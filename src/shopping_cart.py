from dataclasses import dataclass
from typing import List


@dataclass
class CartItem:
    name: str
    price: float
    quantity: int = 1


class ShoppingCart:
    def __init__(self) -> None:
        self._items: List[CartItem] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self._items.append(CartItem(name=name, price=price, quantity=quantity))

    def total_items(self) -> int:
        return sum(item.quantity for item in self._items)

    def total_price(self) -> float:
        return sum(item.price * item.quantity for item in self._items)

    def apply_discount(self, percent: float) -> float:
        """Apply a percentage discount and return the discounted total."""
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")
        total = self.total_price()
        discount_amount = total * (percent / 100)
        return total - discount_amount
