class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price
    
    def to_dict(self):
        return{
            "name": self.name,
            "price": self.price,
            "type": self.__class__.__name__
        }