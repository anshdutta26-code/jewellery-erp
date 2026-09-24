# Jewellery ERP V1

A Streamlit + Supabase jewellery inventory and accounting system built around Tally-style voucher posting.

## What is included

- Company setup and financial-year-aware voucher numbering
- Supabase Auth sign-in / first-account sign-up
- Product Master for jewellery-specific fields
- Category, location, ledger and metal-rate masters
- Excel/CSV Product Master import
- Opening Stock posting
- Sales Voucher with manual transaction-time pricing
- Purchase Voucher
- Receipt, Payment, Contra and Journal vouchers
- Stock Transfer between locations
- Atomic double-entry + stock posting using a PostgreSQL RPC transaction
- Inventory summary derived from immutable stock movements
- Day Book, Trial Balance, Profit & Loss, Balance Sheet, Sales/Purchase registers
- Audit log
- Cancellation architecture (posted vouchers are cancelled, not deleted)

## Architecture

```text
Streamlit UI
   |
   +-- Supabase Auth (anon key, server-side Streamlit session)
   |
   +-- Supabase PostgreSQL (service role key stored only in Streamlit Secrets)
          |
          +-- Masters
          +-- Vouchers / Voucher Entries
          +-- Voucher Items
          +-- Inventory Transactions
          +-- Views / Reports
          +-- Atomic RPC posting
```

## Setup

1. Create a fresh Supabase project for the jewellery business.
2. Run `supabase/schema.sql` in Supabase SQL Editor.
3. Add these values in Streamlit App Settings -> Secrets:

```toml
SUPABASE_URL = "https://YOUR_PROJECT.supabase.co"
SUPABASE_ANON_KEY = "YOUR_ANON_KEY"
SUPABASE_SERVICE_ROLE_KEY = "YOUR_SERVICE_ROLE_KEY"
```

4. Deploy `app.py` on Streamlit Community Cloud.
5. Create/sign in to the first admin account and complete Company Setup.

## First-use sequence

1. Company Setup
2. Categories and locations
3. Product Master / Excel import
4. Customer and Supplier ledgers
5. Opening Stock
6. Purchase / Sales voucher posting

## Pricing model

Product Master does not require a fixed selling price. At each sale, enter the actual taxable value and optional reference fields such as metal rate, making charge, stone value, discount and GST rate. Historical bills remain unchanged when future prices change.

## Accounting behavior

A ₹100,000 taxable sale with 3% GST creates:

```text
Customer / Cash       Dr  103,000
    Sales                 Cr 100,000
    Output GST            Cr   3,000
```

The same voucher creates the linked negative inventory movement. Purchases do the inverse.

## Inventory design

The Product Master supports PIECE, WEIGHT and QUANTITY inventory. Inventory transactions store quantity, gross weight, net weight and value together. Stock balance is calculated from movement history rather than an editable stock field.

## Security

- Never commit `SUPABASE_SERVICE_ROLE_KEY` to GitHub.
- Keep the service role key only in Streamlit Secrets.
- Database posting RPCs are restricted to the service role.
- Posted vouchers are cancelled/reversed rather than physically deleted.
