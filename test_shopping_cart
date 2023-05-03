# test_shopping_cart.py

import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()
        
    def test_add_item(self):
        self.cart.add_item('apple', 1.50)
        self.assertEqual(len(self.cart.items), 1)
        
    def test_remove_item(self):
        self.cart.add_item('apple', 1.50)
        self.cart.remove_item('apple')
        self.assertEqual(len(self.cart.items), 0)
        
    def test_view_cart(self):
        self.cart.add_item('apple', 1.50)
        self.cart.add_item('banana', 0.75)
        self.assertEqual(self.cart.view_cart(), 'apple: 1.50\nbanana: 0.75\n')
        
    def test_calculate_total(self):
        self.cart.add_item('apple', 1.50)
        self.cart.add_item('banana', 0.75)
        self.assertEqual(self.cart.calculate_total(), 2.25)
