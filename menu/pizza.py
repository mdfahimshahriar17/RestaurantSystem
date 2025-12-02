from .base_item import FoodItem


class Pizza(FoodItem):
    def __init__(self, name, price, extra_cheese=False):
        super().__init__(name, price)
    
        self.extra_cheese = extra_cheese #Child class additional attributes



    def get_price(self):
        #method override extra cheese dile price barbe (polymorphism)
        if self.extra_cheese:
            return self.price + 20
        
        return self.price
    


    def to_dict(self):  #Override to dict
        data = super().to_dict()
        data["extra_cheese"] = self.extra_cheese #method extension + override

        return data
    
    