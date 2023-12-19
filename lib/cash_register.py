class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = list()
        self.item_prices = list()
        self.quantities = list()

    def add_item(self, title, price, quantity=1):
        for i in range(quantity):
            self.item_prices.append(price)
            self.quantities.append(quantity)
            self.items.append(title)
        self.total += price * quantity
        return self.items

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total - (self.total * self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.item_prices:
            last_price = self.item_prices.pop()
            last_quantity = self.quantities.pop()
            self.items.pop()
            self.total -= last_price * last_quantity
            self.items.pop()
            if len(self.item_prices) == 0:
                self.total = 0.0
            print(self.total)
            return self.total
        return self.total


new_register = CashRegister()
new_register.add_item("eggs", 1.99, 2)
# new_register.add_item("tomato", 1.76, 3)
new_register.void_last_transaction()