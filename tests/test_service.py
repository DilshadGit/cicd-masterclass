from app.service import BillingService, InvoiceItem

def test_billing_total_calculation():
    service = BillingService(tax_rate=0.10)
    items = [
        InvoiceItem(description="Cloud Server", unit_price=50.0, quantity=2),
        InvoiceItem(description="Static IP", unit_price=10.0, quantity=1)
    ]
    # Subtotal: 100 + 10 = 110. Tax: 11. Total: 121
    assert service.calculate_subtotal(items) == 110.0
    assert service.calculate_tax(110.0) == 11.0
    assert service.calculate_total(items) == 121.0
