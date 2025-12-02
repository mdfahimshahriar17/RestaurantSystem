from .base_item import FoodItem


class Drink(FoodItem):
    def __init__(self, name, price, size="reguler"):
        super().__init__(name, price)

        self.size = size


    def get_price(self):
        if self.size == "large":
            return self.price + 10
        
        elif self.size == "small":
            return self.price - 5
        
        return self.price
    

    def to_dict(self):
        data = super().to_dict()
        data["size"] = self.size

        return data