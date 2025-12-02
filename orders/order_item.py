class OrderItem:
    def __init__(self, item, quantity):
        """
        item = FoodItem / Pizza / Burger / Drink object
        quantity = koto piece
        """
        self.item = item
        self.quantity = quantity


    def get_subtotal(self):
        """Ekta line: item er price * quantity"""

        return self.item.get_price() * self.quantity
    


    def to_dict(self):

        return{
            "name": self.item.name,
            "type": self.item.__class__.__name__,
            "uit_price": self.item.get_price(),
            "quantity": self.quantity,
            "subtotal": self.get_subtotal()
        }