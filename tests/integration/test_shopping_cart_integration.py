from src.shopping_cart import ShoppingCart


def test_checkout_flow_with_discount():
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000.0, quantity=1)
    cart.add_item("Mouse", 50.0, quantity=2)  # 100

    total_before_discount = cart.total_price()
    total_after_discount = cart.apply_discount(10)  # 10%

    assert total_before_discount == 1100.0
    assert total_after_discount == 990.0


def test_add_items_and_check_totals():
    cart = ShoppingCart()
    cart.add_item("Book", 20.0, quantity=2)   # 40
    cart.add_item("Pen", 2.0, quantity=5)     # 10
    cart.add_item("Notebook", 5.0, quantity=1)  # 5

    assert cart.total_items() == 8
    assert cart.total_price() == 55.0

    discounted_total = cart.apply_discount(5)  # 5%
    assert discounted_total == 52.25
