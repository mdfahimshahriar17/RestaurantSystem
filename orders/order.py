from .order_item import OrderItem

VAT_RATE = 0.05

class Order:
    def __init__(self, customer_name=None):
        self.customer_name = customer_name
        self.items = [] #List of order item
        self.is_paid = False


    def add_item(self, item, quantity):
        """item = FoodItem/Pizza/Burger/Drink, quantity = int"""
        order_item = OrderItem(item, quantity)
        self.items.append(order_item)

        print(f"Added {quantity} x {item.name} to order.")


    def get_total(self):
        """sob OrderItem er subtotal jog"""

        return sum(order_item.get_subtotal() for order_item in self.items)


    def print_summary(self):
        print("\n===== ORDER SUMMARY =====")
        if self.customer_name:
            print(f"Customer: {self.customer_name}")

        if not self.items:
            print("No items in order.")

            return
        
        for order_item in self.items:
            print(
                f"{order_item.quantity} x {order_item.item.name}"
                f"= {order_item.get_subtotal()}"
            )

        
        print("-------------------------")
        print(f"TOTAL: {self.get_total()}")
        print("=========================")
        
    VAT_RATE = 0.05  # 5% VAT

class Order:
    ...

    def get_subtotal(self):
        return sum(order_item.get_subtotal() for order_item in self.items)

    def get_vat(self):
        return self.get_subtotal() * VAT_RATE

    def get_total_after_vat(self):
        return self.get_subtotal() + self.get_vat()

    def apply_discount(self, percent):
        """percent = 10 hole 10% discount"""
        discount_amount = self.get_total_after_vat() * (percent / 100)
        return self.get_total_after_vat() - discount_amount


    def to_dict(self):
        return {
            "customer_name": self.customer_name,
            "items": [oi.to_dict() for oi in self.items],
            "total": self.get_total(),
            "is_paid": self.is_paid
        }
