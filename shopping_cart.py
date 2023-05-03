# shopping_cart.py

class ShoppingCart:
    
    def __init__(self):
        self.items = {}
        
    def add_item(self, item, price):
        if item not in self.items:
            self.items[item] = price
            
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            
    def view_cart(self):
        output = ''
        for item, price in self.items.items():
            output += f'{item}: {price:.2f}\n'
        return output
    
    def calculate_total(self):
        return sum(self.items.values())
