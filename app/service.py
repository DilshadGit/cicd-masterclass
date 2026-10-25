"""Business logic service layer"""
from dataclasses import dataclass
from typing import List, Optional
from .calculator import add, multiply

@dataclass
class InvoiceItem:
    description: str
    unit_price: float
    quantity: int

class BillingService:
    def __init__(self, tax_rate: float = 0.20):
        self.tax_rate = tax_rate

    def calculate_subtotal(self, items: List[InvoiceItem]) -> float:
        return sum(multiply(item.unit_price, item.quantity) for item in items)

    def calculate_tax(self, subtotal: float) -> float:
        return multiply(subtotal, self.tax_rate)

    def calculate_total(self, items: List[InvoiceItem]) -> float:
        subtotal = self.calculate_subtotal(items)
        tax = self.calculate_tax(subtotal)
        return add(subtotal, tax)
