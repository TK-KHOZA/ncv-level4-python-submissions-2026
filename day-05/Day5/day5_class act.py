class Product:
    def __init__(self, name, price, quantity):
        # 3 Instance Attributes
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method 1: Calculate total stock value
    def total_value(self):
        return self.price * self.quantity

    # Method 2: Apply a percentage discount
    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)

    # Method 3: Update stock quantity when items are sold
    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return f"Sold {amount} {self.name}(s). Remaining stock: {self.quantity}"
        return f"Not enough stock! Only {self.quantity} available."


# --- Example Usage ---
item = Product("Wireless Mouse", 25.00, 10)

print(f"Total Value: ${item.total_value():.2f}")  # Output: Total Value: $250.00

item.apply_discount(10)  # 10% off
print(f"New Price: ${item.price:.2f}")  # Output: New Price: $22.50

print(item.sell(3))  # Output: Sold 3 Wireless Mouse(s). Remaining stock: 7
