from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP
from typing import Any


def money(value: Any) -> float:
    try:
        return float(Decimal(str(value or 0)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
    except Exception:
        return 0.0


def number(value: Any, places: int = 3) -> float:
    try:
        q = "0." + ("0" * places)
        return float(Decimal(str(value or 0)).quantize(Decimal(q), rounding=ROUND_HALF_UP))
    except Exception:
        return 0.0


def build_sales_posting(
    *,
    party_ledger_id: str,
    sales_ledger_id: str,
    output_tax_ledger_id: str | None,
    items: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], float]:
    taxable = money(sum(money(i.get("taxable_value")) for i in items))
    tax = money(sum(money(i.get("tax_amount")) for i in items))
    total = money(sum(money(i.get("line_total")) for i in items))
    entries: list[dict[str, Any]] = [
        {"ledger_id": party_ledger_id, "debit": total, "credit": 0, "narration": "Sale consideration"},
        {"ledger_id": sales_ledger_id, "debit": 0, "credit": taxable, "narration": "Sales"},
    ]
    if tax:
        if not output_tax_ledger_id:
            raise ValueError("Output GST ledger is required when tax is non-zero")
        entries.append({"ledger_id": output_tax_ledger_id, "debit": 0, "credit": tax, "narration": "Output GST"})

    inventory = []
    for i in items:
        inventory.append({
            "product_id": i["product_id"],
            "location_id": i.get("location_id") or "",
            "transaction_type": "SALE",
            "quantity_delta": -abs(number(i.get("quantity"))),
            "gross_weight_delta": -abs(number(i.get("gross_weight"))),
            "net_weight_delta": -abs(number(i.get("net_weight"))),
            "value_delta": -abs(money(i.get("taxable_value"))),
            "notes": "Sales issue",
        })
    return entries, inventory, total


def build_purchase_posting(
    *,
    party_ledger_id: str,
    purchase_ledger_id: str,
    input_tax_ledger_id: str | None,
    items: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], float]:
    taxable = money(sum(money(i.get("taxable_value")) for i in items))
    tax = money(sum(money(i.get("tax_amount")) for i in items))
    total = money(sum(money(i.get("line_total")) for i in items))
    entries: list[dict[str, Any]] = [
        {"ledger_id": purchase_ledger_id, "debit": taxable, "credit": 0, "narration": "Purchases"},
        {"ledger_id": party_ledger_id, "debit": 0, "credit": total, "narration": "Purchase consideration"},
    ]
    if tax:
        if not input_tax_ledger_id:
            raise ValueError("Input GST ledger is required when tax is non-zero")
        entries.insert(1, {"ledger_id": input_tax_ledger_id, "debit": tax, "credit": 0, "narration": "Input GST"})

    inventory = []
    for i in items:
        inventory.append({
            "product_id": i["product_id"],
            "location_id": i.get("location_id") or "",
            "transaction_type": "PURCHASE",
            "quantity_delta": abs(number(i.get("quantity"))),
            "gross_weight_delta": abs(number(i.get("gross_weight"))),
            "net_weight_delta": abs(number(i.get("net_weight"))),
            "value_delta": abs(money(i.get("taxable_value"))),
            "notes": "Purchase receipt",
        })
    return entries, inventory, total


def balanced(entries: list[dict[str, Any]]) -> bool:
    dr = money(sum(money(x.get("debit")) for x in entries))
    cr = money(sum(money(x.get("credit")) for x in entries))
    return dr == cr and dr > 0
