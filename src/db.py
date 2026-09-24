from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import streamlit as st
from supabase import create_client, Client


@dataclass
class SessionUser:
    id: str
    email: str
    full_name: str | None = None
    company_id: str | None = None
    role: str = "ADMIN"


def _secret(name: str) -> str:
    try:
        value = st.secrets[name]
    except Exception:
        value = None
    if not value:
        raise RuntimeError(f"Missing Streamlit secret: {name}")
    return str(value)


DEFAULT_SUPABASE_URL = "https://uqqokyjckmezqhhxnmri.supabase.co"
DEFAULT_SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVxcW9reWpja21lenFoaHhubXJpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTAyNTI5MDMsImV4cCI6MjEwNTgyODkwM30.GytunIVaZo9wOh2ECfhZ4vx2YPvRIgjLA_SKfARQCGU"


@st.cache_resource(show_spinner=False)
def auth_client() -> Client:
    # The anon key is public by design. Keeping the verified project key here
    # avoids deployment failures caused by an incorrectly copied public key.
    return create_client(DEFAULT_SUPABASE_URL, DEFAULT_SUPABASE_ANON_KEY)


@st.cache_resource(show_spinner=False)
def db_client() -> Client:
    return create_client(_secret("SUPABASE_URL"), _secret("SUPABASE_SERVICE_ROLE_KEY"))


def sign_in(email: str, password: str) -> SessionUser:
    auth = auth_client()
    res = auth.auth.sign_in_with_password({"email": email, "password": password})
    if not res.user:
        raise RuntimeError("Login failed")
    user_id = str(res.user.id)
    try:
        profile = (
            auth
            .table("profiles")
            .select("user_id,company_id,full_name,role,active")
            .eq("user_id", user_id)
            .single()
            .execute()
            .data
        )
    except Exception as exc:
        raise RuntimeError(f"Signed in, but profile access failed: {exc}") from exc
    if profile and not profile.get("active", True):
        raise RuntimeError("This user is inactive")
    return SessionUser(
        id=user_id,
        email=email,
        full_name=(profile or {}).get("full_name"),
        company_id=(profile or {}).get("company_id"),
        role=(profile or {}).get("role") or "ADMIN",
    )


def sign_out() -> None:
    try:
        auth_client().auth.sign_out()
    except Exception:
        pass


def rows(table: str, company_id: str | None = None, columns: str = "*", order: str | None = None) -> list[dict[str, Any]]:
    q = db_client().table(table).select(columns)
    if company_id:
        q = q.eq("company_id", company_id)
    if order:
        q = q.order(order)
    return q.execute().data or []


def insert(table: str, payload: dict[str, Any] | list[dict[str, Any]]) -> Any:
    return db_client().table(table).insert(payload).execute().data


def update(table: str, payload: dict[str, Any], key: str, value: Any) -> Any:
    return db_client().table(table).update(payload).eq(key, value).execute().data


def delete(table: str, key: str, value: Any) -> Any:
    return db_client().table(table).delete().eq(key, value).execute().data


def rpc(name: str, params: dict[str, Any]) -> Any:
    return db_client().rpc(name, params).execute().data


def by_id(table: str, row_id: str, columns: str = "*") -> dict[str, Any] | None:
    return db_client().table(table).select(columns).eq("id", row_id).single().execute().data


def get_profile(user_id: str) -> dict[str, Any] | None:
    # Read the signed-in user's own profile through RLS rather than the service key.
    return auth_client().table("profiles").select("*").eq("user_id", user_id).single().execute().data


def company(company_id: str) -> dict[str, Any] | None:
    return db_client().table("companies").select("*").eq("id", company_id).single().execute().data


def create_company_for_user(user_id: str, company_payload: dict[str, Any]) -> str:
    try:
        admin_db = db_client()
        # Force a lightweight request so an invalid server key produces a clear error.
        admin_db.table("profiles").select("user_id").eq("user_id", user_id).limit(1).execute()
    except Exception as exc:
        raise RuntimeError(
            "The Streamlit SUPABASE_SERVICE_ROLE_KEY is missing or invalid. "
            "Open Streamlit Manage app → Settings → Secrets and replace it with the "
            "Supabase Jewellery ERP service_role/secret key."
        ) from exc

    created = admin_db.table("companies").insert(company_payload).execute().data
    if not created:
        raise RuntimeError("Company could not be created")
    company_id = created[0]["id"]
    admin_db.table("profiles").update({"company_id": company_id, "role": "OWNER"}).eq("user_id", user_id).execute()
    rpc("seed_company_defaults", {"p_company_id": company_id})
    return company_id


def stock_summary(company_id: str) -> list[dict[str, Any]]:
    return db_client().table("v_stock_summary").select("*").eq("company_id", company_id).execute().data or []


def ledger_balances(company_id: str) -> list[dict[str, Any]]:
    return db_client().table("v_ledger_balances").select("*").eq("company_id", company_id).execute().data or []


def voucher_list(company_id: str, limit: int = 250) -> list[dict[str, Any]]:
    return (
        db_client()
        .table("vouchers")
        .select("id,voucher_number,voucher_type,voucher_date,reference_no,status,total_amount,party_ledger_id,created_at")
        .eq("company_id", company_id)
        .order("voucher_date", desc=True)
        .limit(limit)
        .execute()
        .data
        or []
    )


def ledger_entries_for_company(company_id: str) -> list[dict[str, Any]]:
    return (
        db_client()
        .table("voucher_entries")
        .select("id,debit,credit,narration,ledger_id,ledgers(name,group_id,account_groups(name,nature)),vouchers!inner(id,company_id,voucher_number,voucher_type,voucher_date,status)")
        .eq("vouchers.company_id", company_id)
        .eq("vouchers.status", "POSTED")
        .execute()
        .data
        or []
    )
