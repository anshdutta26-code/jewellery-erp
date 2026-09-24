# deployment-refresh: shubhraj-theme
from __future__ import annotations

from datetime import date, datetime
from io import BytesIO
from typing import Any

import pandas as pd
import streamlit as st

from src.accounting import balanced, build_purchase_posting, build_sales_posting, money, number
from src.db import (
    auth_client,
    company,
    create_company_for_user,
    db_client,
    get_profile,
    insert,
    ledger_balances,
    ledger_entries_for_company,
    rows,
    rpc,
    sign_in,
    sign_out,
    stock_summary,
    update,
    voucher_list,
)
from src.style import inject_css, page_header

st.set_page_config(page_title="Shubhraj Jewels ERP", page_icon="💎", layout="wide", initial_sidebar_state="expanded")
inject_css()


def fmt_inr(v: Any) -> str:
    try:
        return f"₹{float(v or 0):,.2f}"
    except Exception:
        return "₹0.00"


def safe_data(executor, default=None):
    try:
        return executor()
    except Exception as exc:
        st.error(str(exc))
        return [] if default is None else default


def require_user():
    if "user" in st.session_state:
        return st.session_state.user

    st.markdown(
        """
        <div class="login-brand">
          <div class="srj-seal" aria-label="Shubhraj Jewels">
            <div class="srj-monogram">SRJ</div>
            <div class="srj-name">SHUBHRAJ</div>
            <div class="srj-jewels">JEWELS</div>
          </div>
          <div class="tag">HERITAGE · CRAFTSMANSHIP · CONTROL</div>
          <div class="headline">Shubhraj Jewels ERP</div>
          <div class="strap">Accounts, inventory and jewellery operations in one secure system.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    tab1, tab2 = st.tabs(["Sign in", "Create first account"])
    with tab1:
        with st.form("login"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Sign in", type="primary", use_container_width=True)
        if submit:
            try:
                st.session_state.user = sign_in(email.strip(), password)
                st.rerun()
            except Exception as exc:
                st.error(f"Sign-in failed: {exc}")

    with tab2:
        st.caption("Use this only for the first administrator. Supabase may require email verification depending on your Auth settings.")
        with st.form("signup"):
            full_name = st.text_input("Full name")
            email2 = st.text_input("Email", key="signup_email")
            password2 = st.text_input("Password", type="password", key="signup_password")
            create = st.form_submit_button("Create account", use_container_width=True)
        if create:
            try:
                res = auth_client().auth.sign_up({"email": email2.strip(), "password": password2, "options": {"data": {"full_name": full_name}}})
                if res.user:
                    st.success("Account created. If email confirmation is enabled in Supabase, confirm the email, then sign in.")
                else:
                    st.warning("Supabase did not return a user. Check your Auth settings.")
            except Exception as exc:
                st.error(str(exc))
    st.stop()


def setup_company_if_needed(user):
    profile = get_profile(user.id) or {}
    current_company_id = profile.get("company_id")
    if current_company_id:
        user.company_id = current_company_id
        user.role = profile.get("role") or user.role
        user.full_name = profile.get("full_name") or user.full_name
        st.session_state.user = user
        return

    page_header("Create your company", "You can edit these details later. Product master and opening stock can remain empty.")
    with st.form("company_setup"):
        name = st.text_input("Company / Firm Name *", value="Shubhraj Jewels")
        legal = st.text_input("Legal Name")
        gstin = st.text_input("GSTIN")
        pan = st.text_input("PAN")
        phone = st.text_input("Phone")
        email = st.text_input("Business Email")
        address = st.text_area("Address")
        state = st.text_input("State")
        pincode = st.text_input("PIN Code")
        submit = st.form_submit_button("Create Company", type="primary")
    if submit:
        if not name.strip():
            st.error("Company name is required.")
        else:
            try:
                cid = create_company_for_user(user.id, {
                    "name": name.strip(), "legal_name": legal.strip() or None, "gstin": gstin.strip() or None,
                    "pan": pan.strip() or None, "phone": phone.strip() or None, "email": email.strip() or None,
                    "address": address.strip() or None, "state": state.strip() or None, "pincode": pincode.strip() or None,
                    "financial_year_start": date(date.today().year if date.today().month >= 4 else date.today().year - 1, 4, 1).isoformat(),
                })
                user.company_id = cid
                user.role = "OWNER"
                st.session_state.user = user
                st.success("Company created with default ledgers and Main Store.")
                st.rerun()
            except Exception as exc:
                st.error(str(exc))
    st.stop()


def get_masters(cid: str):
    ledgers = rows("ledgers", cid, order="name")
    products = rows("products", cid, order="item_name")
    locations = rows("locations", cid, order="name")
    categories = rows("categories", cid, order="name")
    return ledgers, products, locations, categories


def name_map(items: list[dict], id_key="id", name_key="name") -> dict[str, str]:
    return {str(x[id_key]): str(x.get(name_key) or x[id_key]) for x in items}


def find_ledger(ledgers: list[dict], exact_name: str) -> str | None:
    for x in ledgers:
        if str(x.get("name", "")).strip().lower() == exact_name.lower():
            return str(x["id"])
    return None


def dashboard(cid: str):
    page_header("Dashboard", "Sales, stock and accounts — in one controlled view")
    vouchers = voucher_list(cid, 1000)
    stock = stock_summary(cid)
    balances = ledger_balances(cid)
    today = date.today().isoformat()

    sales_today = sum(float(v.get("total_amount") or 0) for v in vouchers if v.get("voucher_type") == "SALE" and v.get("voucher_date") == today and v.get("status") == "POSTED")
    purchases_today = sum(float(v.get("total_amount") or 0) for v in vouchers if v.get("voucher_type") == "PURCHASE" and v.get("voucher_date") == today and v.get("status") == "POSTED")
    stock_value = sum(float(x.get("stock_value") or 0) for x in stock)
    pieces = sum(float(x.get("quantity") or 0) for x in stock)
    net_weight = sum(float(x.get("net_weight") or 0) for x in stock)

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Today's Sales", fmt_inr(sales_today))
    c2.metric("Today's Purchases", fmt_inr(purchases_today))
    c3.metric("Stock Value", fmt_inr(stock_value))
    c4.metric("Stock Qty", f"{pieces:,.3f}")
    c5.metric("Net Metal Weight", f"{net_weight:,.3f} g")

    st.subheader("Recent Vouchers")
    if vouchers:
        df = pd.DataFrame(vouchers)
        show_cols = [c for c in ["voucher_date", "voucher_number", "voucher_type", "reference_no", "status", "total_amount"] if c in df.columns]
        st.dataframe(df[show_cols].head(20), use_container_width=True, hide_index=True)
    else:
        st.info("No vouchers posted yet. Start with Product Master / Opening Stock or create a purchase/sale voucher.")

    st.subheader("Inventory Snapshot")
    if stock:
        sdf = pd.DataFrame(stock)
        cols = [c for c in ["item_code", "item_name", "metal", "purity", "location_name", "quantity", "gross_weight", "net_weight", "stock_value"] if c in sdf.columns]
        st.dataframe(sdf[cols].head(25), use_container_width=True, hide_index=True)
    else:
        st.caption("Opening stock has not been entered yet.")


def masters_page(cid: str):
    page_header("Masters", "Products, categories, locations and accounting ledgers")
    ledgers, products, locations, categories = get_masters(cid)
    tabs = st.tabs(["Product Master", "Categories", "Locations", "Ledgers", "Metal Rates", "Import Products"])

    with tabs[0]:
        c1, c2 = st.columns([0.45, 0.55])
        with c1:
            st.subheader("Add Product")
            catmap = name_map(categories)
            locmap = name_map(locations)
            with st.form("add_product", clear_on_submit=True):
                item_code = st.text_input("Item Code *")
                item_name = st.text_input("Item Name *")
                category = st.selectbox("Category", [""] + list(catmap.keys()), format_func=lambda x: catmap.get(x, "— None —"))
                subcategory = st.text_input("Subcategory")
                metal = st.selectbox("Metal", ["", "Gold", "Silver", "Platinum", "Diamond", "Gemstone", "Other"])
                purity = st.text_input("Purity", placeholder="22K / 18K / 925 / 950")
                tracking = st.selectbox("Tracking Mode", ["PIECE", "WEIGHT", "QUANTITY"])
                unit = st.selectbox("Unit", ["PCS", "GRAM", "CARAT", "PAIR", "SET"])
                w1, w2, w3 = st.columns(3)
                gross = w1.number_input("Gross Wt", min_value=0.0, step=0.001, format="%.3f")
                net = w2.number_input("Net Wt", min_value=0.0, step=0.001, format="%.3f")
                stone = w3.number_input("Stone Wt", min_value=0.0, step=0.001, format="%.3f")
                barcode = st.text_input("Barcode")
                huid = st.text_input("HUID")
                certificate = st.text_input("Certificate No.")
                default_loc = st.selectbox("Default Location", [""] + list(locmap.keys()), format_func=lambda x: locmap.get(x, "— None —"))
                remarks = st.text_area("Remarks")
                add = st.form_submit_button("Add Product", type="primary")
            if add:
                if not item_code.strip() or not item_name.strip():
                    st.error("Item Code and Item Name are required.")
                else:
                    try:
                        insert("products", {
                            "company_id": cid, "item_code": item_code.strip(), "item_name": item_name.strip(),
                            "category_id": category or None, "subcategory": subcategory.strip() or None,
                            "metal": metal or None, "purity": purity.strip() or None, "tracking_mode": tracking, "unit": unit,
                            "gross_weight": gross, "net_weight": net, "stone_weight": stone,
                            "barcode": barcode.strip() or None, "huid": huid.strip() or None,
                            "certificate_no": certificate.strip() or None, "default_location_id": default_loc or None,
                            "remarks": remarks.strip() or None,
                        })
                        st.success("Product added.")
                        st.rerun()
                    except Exception as exc:
                        st.error(str(exc))
        with c2:
            st.subheader(f"Products ({len(products)})")
            if products:
                pdf = pd.DataFrame(products)
                cols = [c for c in ["item_code", "item_name", "metal", "purity", "tracking_mode", "unit", "gross_weight", "net_weight", "barcode", "huid", "active"] if c in pdf.columns]
                st.dataframe(pdf[cols], use_container_width=True, hide_index=True, height=640)
            else:
                st.info("No products yet.")

    with tabs[1]:
        with st.form("category_form", clear_on_submit=True):
            name = st.text_input("Category Name")
            submit = st.form_submit_button("Add Category")
        if submit and name.strip():
            try:
                insert("categories", {"company_id": cid, "name": name.strip()})
                st.rerun()
            except Exception as exc: st.error(str(exc))
        if categories:
            st.dataframe(pd.DataFrame(categories)[["name", "active"]], use_container_width=True, hide_index=True)

    with tabs[2]:
        with st.form("location_form", clear_on_submit=True):
            name = st.text_input("Location Name")
            ltype = st.selectbox("Type", ["STORE", "WAREHOUSE", "COUNTER", "VAULT", "OTHER"])
            submit = st.form_submit_button("Add Location")
        if submit and name.strip():
            try:
                insert("locations", {"company_id": cid, "name": name.strip(), "location_type": ltype})
                st.rerun()
            except Exception as exc: st.error(str(exc))
        if locations:
            st.dataframe(pd.DataFrame(locations)[["name", "location_type", "active"]], use_container_width=True, hide_index=True)

    with tabs[3]:
        groups = rows("account_groups", cid, order="name")
        gmap = name_map(groups)
        with st.form("ledger_form", clear_on_submit=True):
            lname = st.text_input("Ledger Name *")
            group_id = st.selectbox("Group *", list(gmap.keys()), format_func=lambda x: gmap.get(x, x)) if gmap else ""
            party_type = st.selectbox("Party Type", ["", "CUSTOMER", "SUPPLIER", "KARIGAR", "OTHER"])
            gstin = st.text_input("GSTIN")
            phone = st.text_input("Phone")
            opening = st.number_input("Opening Balance", min_value=0.0, step=1.0)
            side = st.radio("Opening Side", ["DR", "CR"], horizontal=True)
            submit = st.form_submit_button("Add Ledger")
        if submit:
            if not lname.strip() or not group_id:
                st.error("Ledger name and group are required.")
            else:
                try:
                    insert("ledgers", {"company_id": cid, "name": lname.strip(), "group_id": group_id, "party_type": party_type or None, "gstin": gstin.strip() or None, "phone": phone.strip() or None, "opening_balance": opening, "opening_side": side})
                    st.rerun()
                except Exception as exc: st.error(str(exc))
        if ledgers:
            ldf = pd.DataFrame(ledgers)
            cols = [c for c in ["name", "party_type", "gstin", "phone", "opening_balance", "opening_side", "active"] if c in ldf.columns]
            st.dataframe(ldf[cols], use_container_width=True, hide_index=True)

    with tabs[4]:
        existing = rows("metal_rates", cid, order="rate_date")
        with st.form("metal_rate", clear_on_submit=True):
            rdate = st.date_input("Date", value=date.today())
            metal = st.selectbox("Metal", ["Gold", "Silver", "Platinum"])
            purity = st.text_input("Purity", value="22K")
            rate = st.number_input("Rate / Gram", min_value=0.0, step=1.0)
            submit = st.form_submit_button("Save Rate")
        if submit:
            try:
                db_client().table("metal_rates").upsert({"company_id": cid, "rate_date": rdate.isoformat(), "metal": metal, "purity": purity.strip(), "rate_per_gram": rate}, on_conflict="company_id,rate_date,metal,purity").execute()
                st.success("Metal rate saved.")
                st.rerun()
            except Exception as exc: st.error(str(exc))
        if existing:
            rdf = pd.DataFrame(existing)
            st.dataframe(rdf[["rate_date", "metal", "purity", "rate_per_gram"]].sort_values("rate_date", ascending=False), use_container_width=True, hide_index=True)

    with tabs[5]:
        st.write("Upload an Excel/CSV product master. Required columns: **item_code, item_name**. Other supported columns are optional.")
        template = pd.DataFrame(columns=["item_code","item_name","category","subcategory","metal","purity","tracking_mode","unit","gross_weight","net_weight","stone_weight","barcode","huid","certificate_no","remarks"])
        bio = BytesIO(); template.to_excel(bio, index=False)
        st.download_button("Download Product Import Template", bio.getvalue(), "product_import_template.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        file = st.file_uploader("Product Master", type=["xlsx", "csv"])
        if file:
            try:
                df = pd.read_excel(file) if file.name.lower().endswith("xlsx") else pd.read_csv(file)
                st.dataframe(df.head(25), use_container_width=True, hide_index=True)
                if st.button("Import Products", type="primary"):
                    if not {"item_code","item_name"}.issubset(set(df.columns)):
                        st.error("item_code and item_name columns are required.")
                    else:
                        category_lookup = {x["name"].lower(): x["id"] for x in categories}
                        payload=[]
                        for _, r in df.fillna("").iterrows():
                            cat = str(r.get("category", "")).strip()
                            if cat and cat.lower() not in category_lookup:
                                created = insert("categories", {"company_id": cid, "name": cat})
                                category_lookup[cat.lower()] = created[0]["id"]
                            payload.append({
                                "company_id": cid, "item_code": str(r["item_code"]).strip(), "item_name": str(r["item_name"]).strip(),
                                "category_id": category_lookup.get(cat.lower()) if cat else None,
                                "subcategory": str(r.get("subcategory", "")).strip() or None,
                                "metal": str(r.get("metal", "")).strip() or None,
                                "purity": str(r.get("purity", "")).strip() or None,
                                "tracking_mode": (str(r.get("tracking_mode", "PIECE")).strip().upper() or "PIECE"),
                                "unit": (str(r.get("unit", "PCS")).strip().upper() or "PCS"),
                                "gross_weight": float(r.get("gross_weight") or 0), "net_weight": float(r.get("net_weight") or 0), "stone_weight": float(r.get("stone_weight") or 0),
                                "barcode": str(r.get("barcode", "")).strip() or None, "huid": str(r.get("huid", "")).strip() or None,
                                "certificate_no": str(r.get("certificate_no", "")).strip() or None, "remarks": str(r.get("remarks", "")).strip() or None,
                            })
                        db_client().table("products").upsert(payload, on_conflict="company_id,item_code").execute()
                        st.success(f"Imported {len(payload)} products.")
                        st.rerun()
            except Exception as exc:
                st.error(f"Import error: {exc}")


def opening_stock_page(cid: str, user_id: str):
    page_header("Opening Stock", "Post opening inventory as a balanced accounting + stock voucher")
    ledgers, products, locations, _ = get_masters(cid)
    if not products:
        st.warning("Create Product Master first.")
        return
    pmap = {p["id"]: f'{p["item_code"]} — {p["item_name"]}' for p in products}
    lmap = name_map(locations)
    inv_ledger = find_ledger(ledgers, "Inventory Asset")
    equity_ledger = find_ledger(ledgers, "Opening Balance Equity")
    if not inv_ledger or not equity_ledger:
        st.error("Default Inventory Asset / Opening Balance Equity ledgers are missing. Re-run seed_company_defaults in Supabase SQL Editor.")
        return
    with st.form("opening_stock"):
        vdate = st.date_input("Opening Date", value=date.today())
        product_id = st.selectbox("Product", list(pmap.keys()), format_func=lambda x: pmap[x])
        p = next(x for x in products if x["id"] == product_id)
        location_id = st.selectbox("Location", list(lmap.keys()), format_func=lambda x: lmap[x]) if lmap else ""
        c1,c2,c3,c4 = st.columns(4)
        qty = c1.number_input("Quantity", min_value=0.0, value=1.0 if p.get("tracking_mode") != "WEIGHT" else 0.0, step=0.001)
        gross = c2.number_input("Gross Weight", min_value=0.0, value=float(p.get("gross_weight") or 0), step=0.001, format="%.3f")
        net = c3.number_input("Net Weight", min_value=0.0, value=float(p.get("net_weight") or 0), step=0.001, format="%.3f")
        value = c4.number_input("Opening Value", min_value=0.0, step=1.0)
        note = st.text_input("Narration", value="Opening stock")
        submit = st.form_submit_button("Post Opening Stock", type="primary")
    if submit:
        if value <= 0 or (qty <= 0 and net <= 0):
            st.error("Enter stock quantity/weight and an opening value greater than zero.")
        else:
            entries=[{"ledger_id": inv_ledger,"debit":money(value),"credit":0,"narration":"Opening inventory"},{"ledger_id":equity_ledger,"debit":0,"credit":money(value),"narration":"Opening balance"}]
            item={"product_id":product_id,"location_id":location_id,"quantity":qty,"gross_weight":gross,"net_weight":net,"unit_price":value/max(qty,1),"taxable_value":value,"line_total":value,"metadata":{"opening":True}}
            inventory=[{"product_id":product_id,"location_id":location_id,"transaction_type":"OPENING_STOCK","quantity_delta":qty,"gross_weight_delta":gross,"net_weight_delta":net,"value_delta":value,"notes":note}]
            try:
                result=rpc("post_voucher", {"p_company_id":cid,"p_voucher_type":"STOCK_JOURNAL","p_voucher_date":vdate.isoformat(),"p_reference_no":"","p_narration":note,"p_party_ledger_id":None,"p_total_amount":money(value),"p_entries":entries,"p_items":[item],"p_inventory":inventory,"p_created_by":user_id})
                st.success(f"Opening stock posted: {result.get('voucher_number') if isinstance(result,dict) else result}")
            except Exception as exc: st.error(str(exc))


def add_item_widget(kind: str, cid: str, products: list[dict], locations: list[dict]):
    key = f"{kind}_cart"
    st.session_state.setdefault(key, [])
    pmap = {p["id"]: f'{p["item_code"]} — {p["item_name"]}' for p in products}
    lmap = name_map(locations)
    if not products:
        st.warning("No products in Product Master.")
        return
    st.markdown("#### Add Item")
    with st.form(f"{kind}_add_item", clear_on_submit=False):
        product_id = st.selectbox("Product", list(pmap.keys()), format_func=lambda x: pmap[x], key=f"{kind}_product")
        product = next(x for x in products if x["id"] == product_id)
        default_loc = product.get("default_location_id") if product.get("default_location_id") in lmap else (next(iter(lmap.keys())) if lmap else "")
        location_id = st.selectbox("Location", list(lmap.keys()), index=list(lmap.keys()).index(default_loc) if default_loc in lmap else 0, format_func=lambda x:lmap[x], key=f"{kind}_location") if lmap else ""
        c1,c2,c3 = st.columns(3)
        qty = c1.number_input("Quantity", min_value=0.0, value=1.0 if product.get("tracking_mode") != "WEIGHT" else 0.0, step=0.001, key=f"{kind}_qty")
        gross = c2.number_input("Gross Wt", min_value=0.0, value=float(product.get("gross_weight") or 0), step=0.001, format="%.3f", key=f"{kind}_gross")
        net = c3.number_input("Net Wt", min_value=0.0, value=float(product.get("net_weight") or 0), step=0.001, format="%.3f", key=f"{kind}_net")
        st.caption("Price is entered at transaction time; Product Master does not need a fixed selling price.")
        c4,c5,c6,c7 = st.columns(4)
        taxable = c4.number_input("Taxable Value *", min_value=0.0, step=100.0, key=f"{kind}_taxable")
        tax_rate = c5.number_input("GST %", min_value=0.0, max_value=100.0, value=3.0, step=0.1, key=f"{kind}_tax")
        making = c6.number_input("Making Charge (record)", min_value=0.0, step=100.0, key=f"{kind}_making")
        stone_value = c7.number_input("Stone Value (record)", min_value=0.0, step=100.0, key=f"{kind}_stone")
        c8,c9 = st.columns(2)
        metal_rate = c8.number_input("Metal Rate / g (record)", min_value=0.0, step=10.0, key=f"{kind}_metal_rate")
        discount = c9.number_input("Discount (record)", min_value=0.0, step=100.0, key=f"{kind}_discount")
        add = st.form_submit_button("Add Line")
    if add:
        if taxable <= 0:
            st.error("Taxable Value must be greater than zero.")
        elif qty <= 0 and net <= 0:
            st.error("Enter quantity or weight.")
        else:
            tax_amount = money(taxable * tax_rate / 100)
            st.session_state[key].append({
                "product_id":product_id,"product_label":pmap[product_id],"location_id":location_id,"location_label":lmap.get(location_id,""),
                "quantity":number(qty),"gross_weight":number(gross),"net_weight":number(net),"unit_price":money(taxable/max(qty,1)),
                "metal_rate":money(metal_rate),"making_charge":money(making),"stone_value":money(stone_value),"other_charge":0,
                "discount":money(discount),"taxable_value":money(taxable),"tax_rate":tax_rate,"tax_amount":tax_amount,"line_total":money(taxable+tax_amount),
                "metadata":{"item_code":product.get("item_code"),"item_name":product.get("item_name")}
            })
            st.rerun()


def cart_table(kind: str):
    key=f"{kind}_cart"; cart=st.session_state.get(key,[])
    if not cart:
        st.info("No lines added yet.")
        return 0.0
    df=pd.DataFrame(cart)
    st.dataframe(df[["product_label","location_label","quantity","gross_weight","net_weight","taxable_value","tax_rate","tax_amount","line_total"]], use_container_width=True, hide_index=True)
    total=money(sum(x["line_total"] for x in cart))
    c1,c2=st.columns([0.7,0.3]); c1.write(""); c2.metric("Voucher Total",fmt_inr(total))
    if st.button("Clear Lines", key=f"clear_{kind}"):
        st.session_state[key]=[]; st.rerun()
    return total


def sales_page(cid: str, user_id: str):
    page_header("Sales Voucher", "Manual selling value at sale time; posting deducts stock and creates accounting entries")
    ledgers, products, locations, _ = get_masters(cid)
    if not ledgers or not products:
        st.warning("Create ledgers and products first."); return
    lmap=name_map(ledgers)
    sales_ledger=find_ledger(ledgers,"Sales"); output_gst=find_ledger(ledgers,"Output GST")
    add_item_widget("sale",cid,products,locations)
    st.markdown("#### Voucher Lines")
    total=cart_table("sale")
    cart=st.session_state.get("sale_cart",[])
    st.markdown("#### Post Voucher")
    party_candidates=[l for l in ledgers if l.get("party_type")=='CUSTOMER' or l.get("name") in ('Cash','Bank')]
    party_ids=[x["id"] for x in party_candidates]
    if not party_ids:
        st.error("Create at least one customer ledger or use default Cash/Bank ledger."); return
    with st.form("post_sale"):
        vdate=st.date_input("Date",value=date.today())
        party=st.selectbox("Customer / Cash / Bank",party_ids,format_func=lambda x:lmap[x])
        ref=st.text_input("Reference / Invoice Ref")
        narration=st.text_input("Narration",value="Jewellery sale")
        post=st.form_submit_button("Post Sales Voucher",type="primary",disabled=not bool(cart))
    if post:
        try:
            summary=stock_summary(cid)
            stock_index={}
            for s in summary:
                k=(s.get("product_id"),s.get("location_id")); stock_index[k]={'qty':float(s.get('quantity') or 0),'net':float(s.get('net_weight') or 0)}
            for line in cart:
                av=stock_index.get((line['product_id'],line.get('location_id')),{'qty':0,'net':0})
                product=next(p for p in products if p['id']==line['product_id'])
                if product.get('tracking_mode') in ('PIECE','QUANTITY') and line['quantity']>av['qty']+1e-9:
                    raise ValueError(f"Insufficient stock for {product['item_code']}. Available {av['qty']}, requested {line['quantity']}.")
                if product.get('tracking_mode')=='WEIGHT' and line['net_weight']>av['net']+1e-9:
                    raise ValueError(f"Insufficient weight stock for {product['item_code']}. Available {av['net']} g.")
            entries,inventory,final_total=build_sales_posting(party_ledger_id=party,sales_ledger_id=sales_ledger,output_tax_ledger_id=output_gst,items=cart)
            if not balanced(entries): raise ValueError("Generated accounting voucher is not balanced.")
            result=rpc("post_voucher",{"p_company_id":cid,"p_voucher_type":"SALE","p_voucher_date":vdate.isoformat(),"p_reference_no":ref,"p_narration":narration,"p_party_ledger_id":party,"p_total_amount":final_total,"p_entries":entries,"p_items":cart,"p_inventory":inventory,"p_created_by":user_id})
            st.session_state.sale_cart=[]
            st.success(f"Sales voucher posted: {result.get('voucher_number') if isinstance(result,dict) else result}")
            st.rerun()
        except Exception as exc: st.error(str(exc))


def purchase_page(cid: str, user_id: str):
    page_header("Purchase Voucher", "Purchase posting increases stock and records supplier liability")
    ledgers, products, locations, _ = get_masters(cid)
    lmap=name_map(ledgers); purchase_ledger=find_ledger(ledgers,"Purchase"); input_gst=find_ledger(ledgers,"Input GST")
    add_item_widget("purchase",cid,products,locations)
    st.markdown("#### Voucher Lines"); cart_table("purchase"); cart=st.session_state.get("purchase_cart",[])
    suppliers=[l for l in ledgers if l.get("party_type")=='SUPPLIER']
    if not suppliers:
        st.warning("Create a supplier ledger in Masters → Ledgers before posting a purchase."); return
    with st.form("post_purchase"):
        vdate=st.date_input("Date",value=date.today(),key="purchase_date")
        party=st.selectbox("Supplier",[x['id'] for x in suppliers],format_func=lambda x:lmap[x])
        ref=st.text_input("Supplier Invoice No.")
        narration=st.text_input("Narration",value="Jewellery purchase")
        post=st.form_submit_button("Post Purchase Voucher",type="primary",disabled=not bool(cart))
    if post:
        try:
            entries,inventory,total=build_purchase_posting(party_ledger_id=party,purchase_ledger_id=purchase_ledger,input_tax_ledger_id=input_gst,items=cart)
            result=rpc("post_voucher",{"p_company_id":cid,"p_voucher_type":"PURCHASE","p_voucher_date":vdate.isoformat(),"p_reference_no":ref,"p_narration":narration,"p_party_ledger_id":party,"p_total_amount":total,"p_entries":entries,"p_items":cart,"p_inventory":inventory,"p_created_by":user_id})
            st.session_state.purchase_cart=[]
            st.success(f"Purchase voucher posted: {result.get('voucher_number') if isinstance(result,dict) else result}")
            st.rerun()
        except Exception as exc: st.error(str(exc))


def accounting_voucher_page(cid: str, user_id: str):
    page_header("Accounting Vouchers", "Receipt, payment, contra and journal entries")
    ledgers=rows("ledgers",cid,order="name"); lmap=name_map(ledgers)
    if len(ledgers)<2: st.warning("At least two ledgers are required."); return
    with st.form("accounting_voucher"):
        vtype=st.selectbox("Voucher Type",["RECEIPT","PAYMENT","CONTRA","JOURNAL"])
        vdate=st.date_input("Date",value=date.today(),key="acct_date")
        debit_ledger=st.selectbox("Debit Ledger",list(lmap.keys()),format_func=lambda x:lmap[x])
        credit_ledger=st.selectbox("Credit Ledger",list(lmap.keys()),format_func=lambda x:lmap[x],index=1 if len(lmap)>1 else 0)
        amount=st.number_input("Amount",min_value=0.0,step=100.0)
        ref=st.text_input("Reference")
        narration=st.text_input("Narration")
        submit=st.form_submit_button("Post Voucher",type="primary")
    if submit:
        if debit_ledger==credit_ledger: st.error("Debit and Credit ledger cannot be the same.")
        elif amount<=0: st.error("Amount must be greater than zero.")
        else:
            entries=[{"ledger_id":debit_ledger,"debit":money(amount),"credit":0,"narration":narration},{"ledger_id":credit_ledger,"debit":0,"credit":money(amount),"narration":narration}]
            try:
                result=rpc("post_voucher",{"p_company_id":cid,"p_voucher_type":vtype,"p_voucher_date":vdate.isoformat(),"p_reference_no":ref,"p_narration":narration,"p_party_ledger_id":None,"p_total_amount":money(amount),"p_entries":entries,"p_items":[],"p_inventory":[],"p_created_by":user_id})
                st.success(f"Posted: {result.get('voucher_number') if isinstance(result,dict) else result}")
            except Exception as exc: st.error(str(exc))


def stock_transfer_page(cid: str, user_id: str):
    page_header("Stock Transfer", "Move jewellery between store, vault, warehouse or counter without changing financial value")
    products=rows("products",cid,order="item_name"); locations=rows("locations",cid,order="name")
    if not products or len(locations)<2:
        st.warning("You need at least one product and two stock locations."); return
    pmap={p['id']:f"{p['item_code']} — {p['item_name']}" for p in products}; lmap=name_map(locations)
    with st.form("stock_transfer"):
        vdate=st.date_input("Date",value=date.today(),key="transfer_date")
        product_id=st.selectbox("Product",list(pmap.keys()),format_func=lambda x:pmap[x])
        from_loc=st.selectbox("From Location",list(lmap.keys()),format_func=lambda x:lmap[x])
        to_loc=st.selectbox("To Location",list(lmap.keys()),format_func=lambda x:lmap[x],index=1)
        product=next(p for p in products if p['id']==product_id)
        c1,c2,c3=st.columns(3)
        qty=c1.number_input("Quantity",min_value=0.0,value=1.0 if product.get('tracking_mode')!='WEIGHT' else 0.0,step=0.001)
        gross=c2.number_input("Gross Weight",min_value=0.0,value=float(product.get('gross_weight') or 0),step=0.001,format="%.3f")
        net=c3.number_input("Net Weight",min_value=0.0,value=float(product.get('net_weight') or 0),step=0.001,format="%.3f")
        note=st.text_input("Narration",value="Stock transfer")
        submit=st.form_submit_button("Post Stock Transfer",type="primary")
    if submit:
        if from_loc==to_loc: st.error("From and To location must be different."); return
        summary=stock_summary(cid); current=next((x for x in summary if x.get('product_id')==product_id and x.get('location_id')==from_loc),None)
        av_qty=float((current or {}).get('quantity') or 0); av_net=float((current or {}).get('net_weight') or 0)
        if product.get('tracking_mode') in ('PIECE','QUANTITY') and qty>av_qty+1e-9:
            st.error(f"Insufficient quantity at {lmap[from_loc]}. Available {av_qty:,.3f}."); return
        if product.get('tracking_mode')=='WEIGHT' and net>av_net+1e-9:
            st.error(f"Insufficient net weight at {lmap[from_loc]}. Available {av_net:,.3f} g."); return
        inventory=[
            {"product_id":product_id,"location_id":from_loc,"transaction_type":"TRANSFER_OUT","quantity_delta":-abs(number(qty)),"gross_weight_delta":-abs(number(gross)),"net_weight_delta":-abs(number(net)),"value_delta":0,"notes":note},
            {"product_id":product_id,"location_id":to_loc,"transaction_type":"TRANSFER_IN","quantity_delta":abs(number(qty)),"gross_weight_delta":abs(number(gross)),"net_weight_delta":abs(number(net)),"value_delta":0,"notes":note},
        ]
        try:
            result=rpc("post_voucher",{"p_company_id":cid,"p_voucher_type":"STOCK_JOURNAL","p_voucher_date":vdate.isoformat(),"p_reference_no":"","p_narration":note,"p_party_ledger_id":None,"p_total_amount":0,"p_entries":[],"p_items":[],"p_inventory":inventory,"p_created_by":user_id})
            st.success(f"Stock transfer posted: {result.get('voucher_number') if isinstance(result,dict) else result}")
        except Exception as exc: st.error(str(exc))

def inventory_page(cid: str):
    page_header("Inventory", "Live stock derived only from inventory transactions")
    stock=stock_summary(cid)
    if not stock:
        st.info("No stock movements yet."); return
    df=pd.DataFrame(stock)
    c1,c2,c3=st.columns(3)
    c1.metric("Total Quantity",f"{df['quantity'].fillna(0).astype(float).sum():,.3f}")
    c2.metric("Net Weight",f"{df['net_weight'].fillna(0).astype(float).sum():,.3f} g")
    c3.metric("Stock Value",fmt_inr(df['stock_value'].fillna(0).astype(float).sum()))
    search=st.text_input("Search item / code / metal")
    if search:
        mask=df.astype(str).apply(lambda col: col.str.contains(search,case=False,na=False)).any(axis=1); df=df[mask]
    cols=[c for c in ["item_code","item_name","metal","purity","tracking_mode","location_name","quantity","gross_weight","net_weight","stock_value"] if c in df.columns]
    st.dataframe(df[cols],use_container_width=True,hide_index=True,height=600)


def reports_page(cid: str):
    page_header("Reports", "Tally-style registers and financial summaries")
    tabs=st.tabs(["Day Book","Trial Balance","Profit & Loss","Balance Sheet","Stock Summary","Sales Register","Purchase Register"])
    vouchers=voucher_list(cid,5000)
    balances=ledger_balances(cid)
    groups=rows("account_groups",cid); group_map={g['id']:g for g in groups}
    ledgers=rows("ledgers",cid); ledger_map={l['id']:l for l in ledgers}

    with tabs[0]:
        if vouchers:
            df=pd.DataFrame(vouchers)
            st.dataframe(df[[c for c in ["voucher_date","voucher_number","voucher_type","reference_no","status","total_amount"] if c in df.columns]],use_container_width=True,hide_index=True)
        else: st.info("No vouchers yet.")
    with tabs[1]:
        if balances:
            bdf=pd.DataFrame(balances)
            bdf['Debit Balance']=bdf['net_dr_balance'].astype(float).clip(lower=0)
            bdf['Credit Balance']=(-bdf['net_dr_balance'].astype(float)).clip(lower=0)
            st.dataframe(bdf[["ledger_name","Debit Balance","Credit Balance"]],use_container_width=True,hide_index=True)
            c1,c2=st.columns(2); c1.metric("Total Debit",fmt_inr(bdf['Debit Balance'].sum())); c2.metric("Total Credit",fmt_inr(bdf['Credit Balance'].sum()))
        else: st.info("No ledger balances yet.")
    with tabs[2]:
        rows_out=[]; total_income=0; total_expense=0
        for b in balances:
            led=ledger_map.get(b['ledger_id'],{}); grp=group_map.get(led.get('group_id'),{}); nature=grp.get('nature'); net=float(b.get('net_dr_balance') or 0)
            if nature=='INCOME':
                amount=max(-net,0); total_income+=amount; rows_out.append({'Ledger':b['ledger_name'],'Type':'Income','Amount':amount})
            elif nature=='EXPENSE':
                amount=max(net,0); total_expense+=amount; rows_out.append({'Ledger':b['ledger_name'],'Type':'Expense','Amount':amount})
        c1,c2,c3=st.columns(3); c1.metric("Income",fmt_inr(total_income)); c2.metric("Expenses",fmt_inr(total_expense)); c3.metric("Net Profit / (Loss)",fmt_inr(total_income-total_expense))
        if rows_out: st.dataframe(pd.DataFrame(rows_out),use_container_width=True,hide_index=True)
    with tabs[3]:
        assets=[]; liabilities=[]
        for b in balances:
            led=ledger_map.get(b['ledger_id'],{}); grp=group_map.get(led.get('group_id'),{}); nature=grp.get('nature'); net=float(b.get('net_dr_balance') or 0)
            if nature=='ASSET': assets.append({'Ledger':b['ledger_name'],'Amount':net})
            elif nature in ('LIABILITY','EQUITY'): liabilities.append({'Ledger':b['ledger_name'],'Amount':-net})
        c1,c2=st.columns(2)
        with c1:
            st.subheader("Assets"); st.dataframe(pd.DataFrame(assets) if assets else pd.DataFrame(columns=['Ledger','Amount']),use_container_width=True,hide_index=True)
        with c2:
            st.subheader("Liabilities & Equity"); st.dataframe(pd.DataFrame(liabilities) if liabilities else pd.DataFrame(columns=['Ledger','Amount']),use_container_width=True,hide_index=True)
        st.caption("V1 financial statements are operational summaries from posted ledgers. Year-end closing, depreciation and statutory finalization can be added later.")
    with tabs[4]: inventory_page(cid)
    with tabs[5]:
        s=[v for v in vouchers if v.get('voucher_type')=='SALE']
        st.dataframe(pd.DataFrame(s) if s else pd.DataFrame(),use_container_width=True,hide_index=True)
    with tabs[6]:
        p=[v for v in vouchers if v.get('voucher_type')=='PURCHASE']
        st.dataframe(pd.DataFrame(p) if p else pd.DataFrame(),use_container_width=True,hide_index=True)


def admin_page(cid: str, user):
    page_header("Admin", "Company settings, user roles and audit trail")
    tabs=st.tabs(["Company","Users","Audit Log","System Check"])
    with tabs[0]:
        comp=company(cid) or {}
        with st.form("company_edit"):
            name=st.text_input("Company Name",value=comp.get('name') or '')
            legal=st.text_input("Legal Name",value=comp.get('legal_name') or '')
            gstin=st.text_input("GSTIN",value=comp.get('gstin') or '')
            pan=st.text_input("PAN",value=comp.get('pan') or '')
            phone=st.text_input("Phone",value=comp.get('phone') or '')
            email=st.text_input("Email",value=comp.get('email') or '')
            address=st.text_area("Address",value=comp.get('address') or '')
            state=st.text_input("State",value=comp.get('state') or '')
            pincode=st.text_input("PIN",value=comp.get('pincode') or '')
            save=st.form_submit_button("Save")
        if save:
            update("companies",{"name":name,"legal_name":legal or None,"gstin":gstin or None,"pan":pan or None,"phone":phone or None,"email":email or None,"address":address or None,"state":state or None,"pincode":pincode or None},"id",cid)
            st.success("Company updated.")
    with tabs[1]:
        profiles=db_client().table("profiles").select("user_id,full_name,role,active,created_at").eq("company_id",cid).execute().data or []
        if profiles: st.dataframe(pd.DataFrame(profiles),use_container_width=True,hide_index=True)
        st.caption("Create additional login users in Supabase → Authentication → Users. Their profile is created automatically; assign company_id and role in the profiles table or extend this screen later.")
    with tabs[2]:
        logs=db_client().table("audit_logs").select("*").eq("company_id",cid).order("created_at",desc=True).limit(500).execute().data or []
        st.dataframe(pd.DataFrame(logs) if logs else pd.DataFrame(),use_container_width=True,hide_index=True)
    with tabs[3]:
        ledgers=rows("ledgers",cid); products=rows("products",cid); locations=rows("locations",cid)
        checks={"Company configured":bool(company(cid)),"Default Cash ledger":bool(find_ledger(ledgers,"Cash")),"Sales ledger":bool(find_ledger(ledgers,"Sales")),"Purchase ledger":bool(find_ledger(ledgers,"Purchase")),"Inventory Asset ledger":bool(find_ledger(ledgers,"Inventory Asset")),"Main stock location":bool(locations),"Products available":bool(products)}
        for k,v in checks.items(): st.write(("✅" if v else "⚠️")+" "+k)


user=require_user(); setup_company_if_needed(user); cid=user.company_id
comp=company(cid) or {"name":"Shubhraj Jewels"}
with st.sidebar:
    st.markdown(
        f"""
        <div class="sidebar-brand">
          <div class="sidebar-monogram">SRJ</div>
          <div class="sidebar-name">{comp.get('name','Shubhraj Jewels').upper()}</div>
          <div class="sidebar-jewels">JEWELS ERP</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(f"{user.full_name or user.email} · {user.role}")
    nav=st.radio("Menu",["Dashboard","Masters","Opening Stock","Sales Voucher","Purchase Voucher","Accounting Vouchers","Stock Transfer","Inventory","Reports","Admin"],label_visibility="collapsed")
    st.divider()
    if st.button("Sign out",use_container_width=True):
        sign_out(); st.session_state.clear(); st.rerun()

try:
    if nav=="Dashboard": dashboard(cid)
    elif nav=="Masters": masters_page(cid)
    elif nav=="Opening Stock": opening_stock_page(cid,user.id)
    elif nav=="Sales Voucher": sales_page(cid,user.id)
    elif nav=="Purchase Voucher": purchase_page(cid,user.id)
    elif nav=="Accounting Vouchers": accounting_voucher_page(cid,user.id)
    elif nav=="Stock Transfer": stock_transfer_page(cid,user.id)
    elif nav=="Inventory": inventory_page(cid)
    elif nav=="Reports": reports_page(cid)
    elif nav=="Admin": admin_page(cid,user)
except Exception as exc:
    st.error(f"Application error: {exc}")
