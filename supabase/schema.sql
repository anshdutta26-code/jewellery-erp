-- Jewellery ERP V1 - Supabase/PostgreSQL schema
-- Run this entire file once in Supabase SQL Editor.

create extension if not exists pgcrypto;

-- ---------- helpers ----------
create or replace function public.financial_year_label(p_date date)
returns text
language sql
immutable
as $$
  select case
    when extract(month from p_date) >= 4
      then lpad((extract(year from p_date)::int % 100)::text, 2, '0') || '-' ||
           lpad(((extract(year from p_date)::int + 1) % 100)::text, 2, '0')
    else lpad(((extract(year from p_date)::int - 1) % 100)::text, 2, '0') || '-' ||
         lpad((extract(year from p_date)::int % 100)::text, 2, '0')
  end;
$$;

create or replace function public.voucher_prefix(p_type text)
returns text
language sql
immutable
as $$
  select case upper(p_type)
    when 'SALE' then 'SALE'
    when 'PURCHASE' then 'PUR'
    when 'RECEIPT' then 'RCT'
    when 'PAYMENT' then 'PMT'
    when 'CONTRA' then 'CTR'
    when 'JOURNAL' then 'JRN'
    when 'STOCK_JOURNAL' then 'STJ'
    when 'SALES_RETURN' then 'SRT'
    when 'PURCHASE_RETURN' then 'PRT'
    else left(upper(regexp_replace(p_type, '[^A-Z0-9]', '', 'g')), 4)
  end;
$$;

-- ---------- company / users ----------
create table if not exists public.companies (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  legal_name text,
  gstin text,
  pan text,
  phone text,
  email text,
  address text,
  state text,
  pincode text,
  currency text not null default 'INR',
  financial_year_start date,
  created_at timestamptz not null default now()
);

create table if not exists public.profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  company_id uuid references public.companies(id) on delete set null,
  full_name text,
  role text not null default 'ADMIN' check (role in ('ADMIN','OWNER','ACCOUNTANT','INVENTORY','SALES','VIEWER')),
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.profiles(user_id, full_name, role)
  values (new.id, coalesce(new.raw_user_meta_data->>'full_name', new.email), 'ADMIN')
  on conflict (user_id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
after insert on auth.users
for each row execute procedure public.handle_new_user();

-- ---------- accounting masters ----------
create table if not exists public.account_groups (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  name text not null,
  nature text not null check (nature in ('ASSET','LIABILITY','INCOME','EXPENSE','EQUITY')),
  parent_name text,
  system_group boolean not null default false,
  unique(company_id, name)
);

create table if not exists public.ledgers (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  name text not null,
  group_id uuid references public.account_groups(id),
  party_type text check (party_type in ('CUSTOMER','SUPPLIER','KARIGAR','OTHER') or party_type is null),
  gstin text,
  phone text,
  email text,
  address text,
  opening_balance numeric(18,2) not null default 0,
  opening_side text not null default 'DR' check (opening_side in ('DR','CR')),
  active boolean not null default true,
  created_at timestamptz not null default now(),
  unique(company_id, name)
);

-- ---------- inventory masters ----------
create table if not exists public.categories (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  name text not null,
  parent_id uuid references public.categories(id) on delete set null,
  active boolean not null default true,
  unique(company_id, name)
);

create table if not exists public.locations (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  name text not null,
  location_type text not null default 'STORE' check (location_type in ('STORE','WAREHOUSE','COUNTER','VAULT','OTHER')),
  active boolean not null default true,
  unique(company_id, name)
);

create table if not exists public.products (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  item_code text not null,
  item_name text not null,
  category_id uuid references public.categories(id) on delete set null,
  subcategory text,
  collection text,
  metal text,
  purity text,
  tracking_mode text not null default 'PIECE' check (tracking_mode in ('PIECE','WEIGHT','QUANTITY')),
  unit text not null default 'PCS',
  gross_weight numeric(18,3) not null default 0,
  net_weight numeric(18,3) not null default 0,
  stone_weight numeric(18,3) not null default 0,
  barcode text,
  huid text,
  certificate_no text,
  default_location_id uuid references public.locations(id) on delete set null,
  opening_cost numeric(18,2) not null default 0,
  active boolean not null default true,
  remarks text,
  created_at timestamptz not null default now(),
  unique(company_id, item_code)
);

create table if not exists public.metal_rates (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  rate_date date not null,
  metal text not null,
  purity text not null,
  rate_per_gram numeric(18,2) not null,
  created_at timestamptz not null default now(),
  unique(company_id, rate_date, metal, purity)
);

-- ---------- vouchers ----------
create table if not exists public.voucher_sequences (
  company_id uuid not null references public.companies(id) on delete cascade,
  voucher_type text not null,
  financial_year text not null,
  last_number bigint not null default 0,
  primary key(company_id, voucher_type, financial_year)
);

create table if not exists public.vouchers (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  voucher_type text not null,
  voucher_number text not null,
  voucher_date date not null,
  reference_no text,
  narration text,
  party_ledger_id uuid references public.ledgers(id) on delete set null,
  status text not null default 'POSTED' check (status in ('DRAFT','POSTED','CANCELLED','REVERSED')),
  total_amount numeric(18,2) not null default 0,
  created_by uuid references auth.users(id) on delete set null,
  created_at timestamptz not null default now(),
  cancelled_at timestamptz,
  unique(company_id, voucher_number)
);

create table if not exists public.voucher_entries (
  id uuid primary key default gen_random_uuid(),
  voucher_id uuid not null references public.vouchers(id) on delete cascade,
  ledger_id uuid not null references public.ledgers(id),
  debit numeric(18,2) not null default 0,
  credit numeric(18,2) not null default 0,
  narration text,
  check (debit >= 0 and credit >= 0),
  check (not (debit > 0 and credit > 0))
);

create table if not exists public.voucher_items (
  id uuid primary key default gen_random_uuid(),
  voucher_id uuid not null references public.vouchers(id) on delete cascade,
  product_id uuid not null references public.products(id),
  location_id uuid references public.locations(id),
  quantity numeric(18,3) not null default 0,
  gross_weight numeric(18,3) not null default 0,
  net_weight numeric(18,3) not null default 0,
  unit_price numeric(18,2) not null default 0,
  metal_rate numeric(18,2) not null default 0,
  making_charge numeric(18,2) not null default 0,
  stone_value numeric(18,2) not null default 0,
  other_charge numeric(18,2) not null default 0,
  discount numeric(18,2) not null default 0,
  taxable_value numeric(18,2) not null default 0,
  tax_rate numeric(8,3) not null default 0,
  tax_amount numeric(18,2) not null default 0,
  line_total numeric(18,2) not null default 0,
  metadata jsonb not null default '{}'::jsonb
);

create table if not exists public.inventory_transactions (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.companies(id) on delete cascade,
  voucher_id uuid references public.vouchers(id) on delete set null,
  product_id uuid not null references public.products(id),
  location_id uuid references public.locations(id),
  transaction_date date not null,
  transaction_type text not null,
  quantity_delta numeric(18,3) not null default 0,
  gross_weight_delta numeric(18,3) not null default 0,
  net_weight_delta numeric(18,3) not null default 0,
  value_delta numeric(18,2) not null default 0,
  notes text,
  created_at timestamptz not null default now()
);

create table if not exists public.audit_logs (
  id bigserial primary key,
  company_id uuid references public.companies(id) on delete cascade,
  user_id uuid references auth.users(id) on delete set null,
  action text not null,
  entity_type text not null,
  entity_id text,
  payload jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index if not exists idx_vouchers_company_date on public.vouchers(company_id, voucher_date desc);
create index if not exists idx_entries_voucher on public.voucher_entries(voucher_id);
create index if not exists idx_items_voucher on public.voucher_items(voucher_id);
create index if not exists idx_inventory_product on public.inventory_transactions(company_id, product_id, transaction_date);
create index if not exists idx_inventory_location on public.inventory_transactions(company_id, location_id, transaction_date);

-- ---------- atomic voucher posting RPC ----------
create or replace function public.post_voucher(
  p_company_id uuid,
  p_voucher_type text,
  p_voucher_date date,
  p_reference_no text,
  p_narration text,
  p_party_ledger_id uuid,
  p_total_amount numeric,
  p_entries jsonb,
  p_items jsonb,
  p_inventory jsonb,
  p_created_by uuid
)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_fy text;
  v_seq bigint;
  v_number text;
  v_voucher_id uuid;
  v_debit numeric(18,2);
  v_credit numeric(18,2);
  r jsonb;
begin
  if p_company_id is null or p_voucher_type is null or p_voucher_date is null then
    raise exception 'Company, voucher type and voucher date are required';
  end if;

  select coalesce(sum((x->>'debit')::numeric),0), coalesce(sum((x->>'credit')::numeric),0)
    into v_debit, v_credit
  from jsonb_array_elements(coalesce(p_entries, '[]'::jsonb)) x;

  if round(v_debit,2) <> round(v_credit,2) then
    raise exception 'Voucher is not balanced. Debit %, Credit %', v_debit, v_credit;
  end if;

  if v_debit = 0 and not (upper(p_voucher_type) = 'STOCK_JOURNAL' and jsonb_array_length(coalesce(p_inventory, '[]'::jsonb)) > 0) then
    raise exception 'Voucher cannot have zero value unless it is a stock journal';
  end if;

  v_fy := public.financial_year_label(p_voucher_date);

  insert into public.voucher_sequences(company_id, voucher_type, financial_year, last_number)
  values (p_company_id, upper(p_voucher_type), v_fy, 1)
  on conflict (company_id, voucher_type, financial_year)
  do update set last_number = public.voucher_sequences.last_number + 1
  returning last_number into v_seq;

  v_number := public.voucher_prefix(p_voucher_type) || '/' || v_fy || '/' || lpad(v_seq::text, 6, '0');

  insert into public.vouchers(
    company_id, voucher_type, voucher_number, voucher_date, reference_no,
    narration, party_ledger_id, status, total_amount, created_by
  ) values (
    p_company_id, upper(p_voucher_type), v_number, p_voucher_date, nullif(p_reference_no,''),
    nullif(p_narration,''), p_party_ledger_id, 'POSTED', coalesce(p_total_amount, v_debit), p_created_by
  ) returning id into v_voucher_id;

  for r in select * from jsonb_array_elements(coalesce(p_entries, '[]'::jsonb)) loop
    insert into public.voucher_entries(voucher_id, ledger_id, debit, credit, narration)
    values (
      v_voucher_id,
      (r->>'ledger_id')::uuid,
      coalesce((r->>'debit')::numeric,0),
      coalesce((r->>'credit')::numeric,0),
      nullif(r->>'narration','')
    );
  end loop;

  for r in select * from jsonb_array_elements(coalesce(p_items, '[]'::jsonb)) loop
    insert into public.voucher_items(
      voucher_id, product_id, location_id, quantity, gross_weight, net_weight,
      unit_price, metal_rate, making_charge, stone_value, other_charge, discount,
      taxable_value, tax_rate, tax_amount, line_total, metadata
    ) values (
      v_voucher_id,
      (r->>'product_id')::uuid,
      nullif(r->>'location_id','')::uuid,
      coalesce((r->>'quantity')::numeric,0),
      coalesce((r->>'gross_weight')::numeric,0),
      coalesce((r->>'net_weight')::numeric,0),
      coalesce((r->>'unit_price')::numeric,0),
      coalesce((r->>'metal_rate')::numeric,0),
      coalesce((r->>'making_charge')::numeric,0),
      coalesce((r->>'stone_value')::numeric,0),
      coalesce((r->>'other_charge')::numeric,0),
      coalesce((r->>'discount')::numeric,0),
      coalesce((r->>'taxable_value')::numeric,0),
      coalesce((r->>'tax_rate')::numeric,0),
      coalesce((r->>'tax_amount')::numeric,0),
      coalesce((r->>'line_total')::numeric,0),
      coalesce(r->'metadata','{}'::jsonb)
    );
  end loop;

  for r in select * from jsonb_array_elements(coalesce(p_inventory, '[]'::jsonb)) loop
    insert into public.inventory_transactions(
      company_id, voucher_id, product_id, location_id, transaction_date, transaction_type,
      quantity_delta, gross_weight_delta, net_weight_delta, value_delta, notes
    ) values (
      p_company_id,
      v_voucher_id,
      (r->>'product_id')::uuid,
      nullif(r->>'location_id','')::uuid,
      p_voucher_date,
      coalesce(nullif(r->>'transaction_type',''), upper(p_voucher_type)),
      coalesce((r->>'quantity_delta')::numeric,0),
      coalesce((r->>'gross_weight_delta')::numeric,0),
      coalesce((r->>'net_weight_delta')::numeric,0),
      coalesce((r->>'value_delta')::numeric,0),
      nullif(r->>'notes','')
    );
  end loop;

  insert into public.audit_logs(company_id, user_id, action, entity_type, entity_id, payload)
  values (p_company_id, p_created_by, 'POST', 'VOUCHER', v_voucher_id::text,
          jsonb_build_object('voucher_number', v_number, 'voucher_type', upper(p_voucher_type), 'amount', p_total_amount));

  return jsonb_build_object('voucher_id', v_voucher_id, 'voucher_number', v_number);
end;
$$;

-- ---------- views ----------
create or replace view public.v_stock_summary as
select
  it.company_id,
  it.product_id,
  p.item_code,
  p.item_name,
  p.metal,
  p.purity,
  p.tracking_mode,
  p.unit,
  it.location_id,
  l.name as location_name,
  sum(it.quantity_delta) as quantity,
  sum(it.gross_weight_delta) as gross_weight,
  sum(it.net_weight_delta) as net_weight,
  sum(it.value_delta) as stock_value
from public.inventory_transactions it
join public.products p on p.id = it.product_id
left join public.locations l on l.id = it.location_id
left join public.vouchers v on v.id = it.voucher_id
where coalesce(v.status, 'POSTED') <> 'CANCELLED'
group by it.company_id, it.product_id, p.item_code, p.item_name, p.metal, p.purity, p.tracking_mode, p.unit, it.location_id, l.name;

create or replace view public.v_ledger_balances as
select
  l.company_id,
  l.id as ledger_id,
  l.name as ledger_name,
  l.group_id,
  l.opening_balance,
  l.opening_side,
  coalesce(sum(case when v.status='POSTED' then e.debit else 0 end),0) as total_debit,
  coalesce(sum(case when v.status='POSTED' then e.credit else 0 end),0) as total_credit,
  (case when l.opening_side='DR' then l.opening_balance else -l.opening_balance end)
    + coalesce(sum(case when v.status='POSTED' then e.debit - e.credit else 0 end),0) as net_dr_balance
from public.ledgers l
left join public.voucher_entries e on e.ledger_id = l.id
left join public.vouchers v on v.id = e.voucher_id
group by l.company_id, l.id, l.name, l.group_id, l.opening_balance, l.opening_side;

-- ---------- default masters helper ----------
create or replace function public.seed_company_defaults(p_company_id uuid)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  g_cash uuid; g_bank uuid; g_sundry_debtors uuid; g_sundry_creditors uuid;
  g_sales uuid; g_purchase uuid; g_duties uuid; g_expense uuid; g_capital uuid; g_current_assets uuid;
begin
  insert into public.account_groups(company_id,name,nature,system_group) values
    (p_company_id,'Current Assets','ASSET',true),
    (p_company_id,'Cash-in-Hand','ASSET',true),
    (p_company_id,'Bank Accounts','ASSET',true),
    (p_company_id,'Sundry Debtors','ASSET',true),
    (p_company_id,'Sundry Creditors','LIABILITY',true),
    (p_company_id,'Sales Accounts','INCOME',true),
    (p_company_id,'Purchase Accounts','EXPENSE',true),
    (p_company_id,'Duties & Taxes','LIABILITY',true),
    (p_company_id,'Indirect Expenses','EXPENSE',true),
    (p_company_id,'Capital Account','EQUITY',true)
  on conflict(company_id,name) do nothing;

  select id into g_current_assets from public.account_groups where company_id=p_company_id and name='Current Assets';
  select id into g_cash from public.account_groups where company_id=p_company_id and name='Cash-in-Hand';
  select id into g_bank from public.account_groups where company_id=p_company_id and name='Bank Accounts';
  select id into g_sales from public.account_groups where company_id=p_company_id and name='Sales Accounts';
  select id into g_purchase from public.account_groups where company_id=p_company_id and name='Purchase Accounts';
  select id into g_duties from public.account_groups where company_id=p_company_id and name='Duties & Taxes';

  insert into public.ledgers(company_id,name,group_id) values
    (p_company_id,'Cash',g_cash),
    (p_company_id,'Bank',g_bank),
    (p_company_id,'Sales',g_sales),
    (p_company_id,'Purchase',g_purchase),
    (p_company_id,'Output GST',g_duties),
    (p_company_id,'Input GST',g_duties),
    (p_company_id,'Inventory Asset',g_current_assets),
    (p_company_id,'Opening Balance Equity',(select id from public.account_groups where company_id=p_company_id and name='Capital Account'))
  on conflict(company_id,name) do nothing;

  insert into public.locations(company_id,name,location_type)
  values (p_company_id,'Main Store','STORE')
  on conflict(company_id,name) do nothing;
end;
$$;

-- Service-role Streamlit app uses server-side key. Restrict direct anonymous access.
alter table public.companies enable row level security;
alter table public.profiles enable row level security;
alter table public.account_groups enable row level security;
alter table public.ledgers enable row level security;
alter table public.categories enable row level security;
alter table public.locations enable row level security;
alter table public.products enable row level security;
alter table public.metal_rates enable row level security;
alter table public.vouchers enable row level security;
alter table public.voucher_entries enable row level security;
alter table public.voucher_items enable row level security;
alter table public.inventory_transactions enable row level security;
alter table public.audit_logs enable row level security;

-- Profiles: authenticated users may read their own profile using the anon/JWT client.
drop policy if exists profile_self_read on public.profiles;
create policy profile_self_read on public.profiles for select to authenticated using (auth.uid() = user_id);

-- ---------- cancellation (never delete posted vouchers) ----------
create or replace function public.cancel_voucher(
  p_company_id uuid,
  p_voucher_id uuid,
  p_user_id uuid,
  p_reason text
)
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  v_number text;
  v_status text;
begin
  select voucher_number, status into v_number, v_status
  from public.vouchers
  where id=p_voucher_id and company_id=p_company_id
  for update;

  if v_number is null then raise exception 'Voucher not found'; end if;
  if v_status <> 'POSTED' then raise exception 'Only POSTED vouchers can be cancelled'; end if;

  update public.vouchers set status='CANCELLED', cancelled_at=now(), narration=concat_ws(' | ', narration, 'CANCELLED: '||coalesce(p_reason,'No reason'))
  where id=p_voucher_id;

  insert into public.audit_logs(company_id,user_id,action,entity_type,entity_id,payload)
  values(p_company_id,p_user_id,'CANCEL','VOUCHER',p_voucher_id::text,jsonb_build_object('voucher_number',v_number,'reason',p_reason));
end;
$$;

-- RPC permissions: server-side service role only.
revoke execute on function public.post_voucher(uuid,text,date,text,text,uuid,numeric,jsonb,jsonb,jsonb,uuid) from public, anon, authenticated;
grant execute on function public.post_voucher(uuid,text,date,text,text,uuid,numeric,jsonb,jsonb,jsonb,uuid) to service_role;
revoke execute on function public.seed_company_defaults(uuid) from public, anon, authenticated;
grant execute on function public.seed_company_defaults(uuid) to service_role;
revoke execute on function public.cancel_voucher(uuid,uuid,uuid,text) from public, anon, authenticated;
grant execute on function public.cancel_voucher(uuid,uuid,uuid,text) to service_role;


-- ---------- production hardening ----------
alter function public.financial_year_label(date) set search_path = public, pg_temp;
alter function public.voucher_prefix(text) set search_path = public, pg_temp;
alter table public.voucher_sequences enable row level security;
alter view public.v_stock_summary set (security_invoker = true);
alter view public.v_ledger_balances set (security_invoker = true);
revoke execute on function public.handle_new_user() from public, anon, authenticated;

drop policy if exists profile_self_read on public.profiles;
create policy profile_self_read on public.profiles
for select to authenticated
using ((select auth.uid()) = user_id);

create index if not exists idx_audit_logs_company on public.audit_logs(company_id);
create index if not exists idx_audit_logs_user on public.audit_logs(user_id);
create index if not exists idx_categories_parent on public.categories(parent_id);
create index if not exists idx_inventory_location_fk on public.inventory_transactions(location_id);
create index if not exists idx_inventory_product_fk on public.inventory_transactions(product_id);
create index if not exists idx_inventory_voucher on public.inventory_transactions(voucher_id);
create index if not exists idx_ledgers_group on public.ledgers(group_id);
create index if not exists idx_products_category on public.products(category_id);
create index if not exists idx_products_default_location on public.products(default_location_id);
create index if not exists idx_profiles_company on public.profiles(company_id);
create index if not exists idx_voucher_entries_ledger on public.voucher_entries(ledger_id);
create index if not exists idx_voucher_items_location on public.voucher_items(location_id);
create index if not exists idx_voucher_items_product on public.voucher_items(product_id);
create index if not exists idx_vouchers_created_by on public.vouchers(created_by);
create index if not exists idx_vouchers_party_ledger on public.vouchers(party_ledger_id);


-- ---------- username login ----------
alter table public.profiles add column if not exists username text;

update public.profiles p
set username = lower(regexp_replace(split_part(u.email, '@', 1), '[^a-z0-9_]+', '', 'g'))
from auth.users u
where p.user_id = u.id
  and (p.username is null or btrim(p.username) = '');

create unique index if not exists profiles_username_lower_uidx
on public.profiles (lower(username))
where username is not null;

create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.profiles(user_id, full_name, username, role)
  values (
    new.id,
    coalesce(new.raw_user_meta_data->>'full_name', new.email),
    nullif(lower(regexp_replace(coalesce(new.raw_user_meta_data->>'username',''), '[^a-z0-9_]+', '', 'g')), ''),
    'ADMIN'
  )
  on conflict (user_id) do update
  set
    full_name = excluded.full_name,
    username = coalesce(public.profiles.username, excluded.username);
  return new;
end;
$$;

create or replace function public.resolve_login_email(p_username text)
returns text
language sql
security definer
set search_path = public, auth
stable
as $$
  select u.email
  from public.profiles p
  join auth.users u on u.id = p.user_id
  where lower(p.username) = lower(btrim(p_username))
    and p.active = true
  limit 1;
$$;

revoke execute on function public.resolve_login_email(text) from public;
grant execute on function public.resolve_login_email(text) to anon, authenticated;
