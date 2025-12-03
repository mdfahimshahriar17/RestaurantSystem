from menu.burger import Burger
from menu.drink import Drink
from orders.order import Order
from orders.order_manager import OrderManager

# Sample items
b1 = Burger("Beef Double Cheese Burger", 150, double_patty=True, extra_cheese=True)
d1 = Drink("Coke", 40, size="large")

# Order create
order = Order(customer_name="Test Customer")
order.add_item(b1, 2)   # 2 burger
order.add_item(d1, 3)   # 3 coke

# Manager use
manager = OrderManager()
manager.save_order(order)       # file e save
manager.list_orders()           # history show
manager.show_order_details(1)   # first order er details
