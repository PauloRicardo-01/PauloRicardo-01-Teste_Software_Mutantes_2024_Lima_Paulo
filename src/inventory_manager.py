class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_name, quantity):
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

    def sell_product(self, product_name, quantity):
        if product_name in self.inventory and self.inventory[product_name] >= quantity:
            self.inventory[product_name] -= quantity
            return True
        return False

    def check_stock(self, product_name):
        return self.inventory.get(product_name, 0) > 0
