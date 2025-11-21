import pytest
from src.shopping_cart import ShoppingCart


def test_add_single_item_increases_total_items():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.0, quantity=2)

    assert cart.total_items() == 2


def test_add_multiple_items_sums_quantities():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.0, quantity=2)
    cart.add_item("Banana", 0.5, quantity=3)

    assert cart.total_items() == 5


def test_total_price_calculates_correctly():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.0, quantity=2)   # 2.0
    cart.add_item("Banana", 0.5, quantity=3)  # 1.5

    assert cart.total_price() == 3.5


def test_apply_discount_valid_range():
    cart = ShoppingCart()
    cart.add_item("Item", 100.0, quantity=1)

    discounted = cart.apply_discount(10)  # 10% kedvezmény

    assert discounted == 90.0


def test_add_item_negative_price_raises_error():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("Invalid", -1.0, quantity=1)


def test_add_item_zero_quantity_raises_error():
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("Invalid", 1.0, quantity=0)
