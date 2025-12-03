import json
import os
from datetime import datetime


from .order import Order


class OrderManager:
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), "order.json")

    def _load_all(self):
        """Read all orders from orders.json (as list of dicts)"""

        try:
            with open(self.data_file, "r") as f:
                return json.load(f)
            
        except:
            return []
        
    def _save_all(self, orders_list):
        """Write full orders list to orders.json"""

        with open(self.data_file, "w") as f:
            json.dump(orders_list, f, indent=4)


    def save_order(self, order: Order):
        """One order ke json e save korbo (append style)"""
        all_orders = self._load_all()

        order_data = order.to_dict()
        
        #extra meta info add korlam
        order_data["order_id"] = len(all_orders) + 1
        order_data["created_at"] = datetime.now().isoformat(timespec="seconds")

        all_orders.append(order_data)
        self._save_all(all_orders)

        print(f"Order #{order_data['order_id']} saved successfully!")



    def list_orders(self):
        """History: shudhu order summary show korbo"""
        all_orders = self._load_all()

        if not all_orders:
            print("No orders found.")
            return
        
        print("\n===== ORDER HISTORY =====")
        for o in all_orders:
            oid = o.get("order_id", "?")
            name = o.get("customer_name") or "Unknown"
            total = o.get("total", 0)
            created = o.get("created_at", "")

            print(f"#{oid} | {name} | Total: {total} | {created}")
           
        print("=========================")




    def show_order_details(self, order_id: int):
        """Specific ekta order er full detail show korbo"""

        all_orders = self._load_all()

        for o in all_orders:
            if o.get("order_id") == order_id:
                print(f"\n=== ORDER #{order_id} DETAILS ===")
                name = o.get("customer_name") or "Unknown"
                print(f"Customer: {name}")


                items = o.get("items", [])
                if not items:
                    print("No items.")
                else:
                    for it in items:
                        q = it.get("quantity")
                        nm = it.get("name")
                        sub = it.get("subtotal")
                        print(f"{q} x {nm} = {sub}")


                print("-------------------------")
                print(f"TOTAL: {o.get('total', 0)}")
                print(f"Paid: {o.get('is_paid', False)}")
                print("=========================\n")
                return
    
        print(f"❌ Order #{order_id} not found.")

    