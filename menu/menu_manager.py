import json
import os

from .base_item import FoodItem
from .burger import Burger
from .pizza import Pizza
from .drink import Drink


class MenuManager:
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), "menu.json")
        self.menu_items = []
        self.load_menu()


    def load_menu(self):
        """Load menu.json and recreate objects"""

        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.menu_items = [self.create_item_from_dict(item) for item in data]

        except:
            self.menu_items = []


    def save_menu(self):
        """Save all item to menu.json"""
        data = [item.to_dict() for item in self.menu_items]
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    
    def create_item_from_dict(self, data):
        """Recreate Pizza/Burger/Drink based on type"""
        item_type = data.get("type")

        if item_type == "Pizza":
            return Pizza(data["name"], data["price"], data.get("extra_cheese", False))

        elif item_type == "Burger":
            return Burger(
                data["name"],
                data["price"],
                data.get("double_patty", False),
                data.get("extra_cheese", False)
            )
        
        elif item_type == "Drink":
            return Drink(
                data["name"],
                data["price"],
                data.get("size", "reguler")
            )
        
        else:
            return FoodItem(data["name"], data["price"] )
        

    def add_item(self, item):
        """Add pizza, drink, burger etc."""
        self.menu_items.append(item)
        self.save_menu()
        print(f"Added: {item.name}")

    
    def list_menu(self):
        if not self.menu_items:
            print("Menu is empty.")
            return
        

        print("\n===== Menu Items =====")
        for item in self.menu_items:
            print(f"{item.name} - {item.get_price()} ({item.__class__.__name__})")



    def search(self, name):
        """Search item by name"""

        results = [item for item in self.menu_items if name.lower() in item.name.lower()]
        return results
