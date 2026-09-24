from src.accounting import balanced, build_purchase_posting, build_sales_posting

ITEMS=[{"product_id":"p1","location_id":"l1","quantity":1,"gross_weight":10,"net_weight":9,"taxable_value":100000,"tax_amount":3000,"line_total":103000}]

def test_sales_balances():
    entries, inv, total=build_sales_posting(party_ledger_id="cash",sales_ledger_id="sales",output_tax_ledger_id="gst",items=ITEMS)
    assert balanced(entries)
    assert total==103000
    assert inv[0]["quantity_delta"]==-1

def test_purchase_balances():
    entries, inv, total=build_purchase_posting(party_ledger_id="supplier",purchase_ledger_id="purchase",input_tax_ledger_id="gst",items=ITEMS)
    assert balanced(entries)
    assert total==103000
    assert inv[0]["quantity_delta"]==1
