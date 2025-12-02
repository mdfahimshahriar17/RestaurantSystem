from .base_item import FoodItem


class Burger(FoodItem):
    def __init__(self, name, price, double_patty=False, extra_cheese=False):
        super().__init__(name, price)
    
        self.double_patty = double_patty
        self.extra_cheese = extra_cheese


    def get_price(self):
        total = self.price

        #extra patty price
        if self.double_patty:
            total += 30

        #extra cheese price
        if self.extra_cheese:
            total += 20

        return total
    

    def to_dict(self):
        data = super().to_dict()
        data["double_patty"] = self.double_patty
        data["extra_cheese"] = self.extra_cheese
    

        return data