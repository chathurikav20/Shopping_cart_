# test_shopping_cart.py

import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Item 1")
        self.assertIn("Item 1", self.cart.items)

    def test_add_multiple_items(self):
        self.cart.add_item("Item 1")
        self.cart.add_item("Item 2")
        self.cart.add_item("Item 3")
        self.assertIn("Item 1", self.cart.items)
        self.assertIn("Item 2", self.cart.items)
        self.assertIn("Item 3", self.cart.items)

    def test_view_cart(self):
        self.cart.add_item("Item 1")
        self.cart.add_item("Item 2")
        self.assertEqual(self.cart.view_cart(), "Item 1, Item 2")

    def test_calculate_total_price(self):
        self.cart.add_item({"name": "Item 1", "price": 10})
        self.cart.add_item({"name": "Item 2", "price": 20})
        self.assertEqual(self.cart.calculate_total_price(), 30)

if __name__ == '__main__':
    unittest.main()
