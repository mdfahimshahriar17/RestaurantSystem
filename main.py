from users.user import UserManager
from menu.menu_manager import MenuManager
from menu.pizza import Pizza
from menu.burger import Burger
from menu.drink import Drink
from orders.order import Order
from orders.order_manager import OrderManager


def main_menu(current_user):
    print("==== Restaurant Management System ====")


    if current_user:
        print(f"Logged in as: {current_user.username} ({current_user.role})")
    else:
        print("Not logged in.")


    print("1. Register User")
    print("2. Login")
    print("3. List Users")
    print("4. Add Menu Item")
    print("5. Show Menu")
    print("6. Search Menu")
    print("7. Create Order")
    print("8. View Order History")
    print("9. Exit")



def main():
    user_manager = UserManager()
    menu_manager = MenuManager()
    order_manager = OrderManager()
    current_user = None #ekhane amra k login ache seta rakhbo

    while True:
        main_menu(current_user)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Role (admin/cashier): ").lower()
            user_manager.register_user(username, password, role)
        
        
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = user_manager.authenticate(username, password)

            if user:
                current_user = user
                print(f"Login successful! Welcome, {user.username} ({user.role})")

            else:
                print("Invalid username or password")


        elif choice == "3":
            user_manager.list_users()

        

        elif choice == "4":
            print("\n--- Add Menu Item ---")
            print("1. Pizza")
            print("2. Burger")
            print("3. Drink")

            item_type = input("Choose item type: ")

            name = input("Enter item name: ")
            price = float(input("Enter base price:  "))

            if item_type == "1":
                extra = input("Extra cheese? (y/n): ").lower() == "y"
                item = Pizza(name, price, extra_cheese=extra)

            elif item_type == "2":
                dp = input("Double patty? (y/n): ").lower() == "y"
                ec = input("Extra cheese? (y/n): ").lower() == "y"
                item = Burger(name, price, double_patty=dp, extra_cheese=ec)

            elif item_type == "3":
                size = input("Size (small/regular/large): ").lower()
                item = Drink(name, price, size=size)

            else:
                print("Invalid type!")
                continue


            menu_manager.add_item(item)


        elif choice == "5":
            menu_manager.list_menu()


        elif choice == "6":
            key = input("Enter name to search: ")
            results = menu_manager.search(key)

            if results:
                print("\n-- Search Results --")
                for item in results:
                    print(f"{item.name} - {item.get_price()} ({item.__class__.__name__})")

            else:
                print("No item found.")



        elif choice =="7":
            #Create new order
            if not menu_manager.menu_items:
                print("Menu is empty. Add some items first.")
                continue

            customer_name = input("Customer name (optional): ").strip() or None
            order = Order(customer_name=customer_name)

            while True:
                print("\n--- Select item for order ---")
                # showing menu with index
                for idx, item in enumerate(menu_manager.menu_items, start=1):
                    print(f"{idx}. {item.name} - {item.get_price()} ({item.__class__.__name__})")

                choice_item = input("Enter item number (or 'q' to finish): ").strip()
                if choice_item.lower() == "q":
                    break

                if not choice_item.isdigit():
                    print("Invalid choice.")
                    continue

                idx = int(choice_item)
                if not (1 <= idx <= len(menu_manager.menu_items)):
                    print("Invalid item number")
                    continue

                #quantity nicchi
                try:
                    qty = int(input("Quantity: "))
                    if qty <= 0:
                        print("Quantity must be positive.")
                        continue

                except ValueError:
                    print("Invalid quantity.")
                    continue
                
                item = menu_manager.menu_items[idx - 1]
                order.add_item(item, qty)

                
            # order summary & save
            if not order.items:
                print("No items in order. Order cancelled.")

            else:
                order.print_summary()
                confirm = input("Save this order? (y/n): ").lower()
                
                if confirm == "y":
                    order_manager.save_order(order)

                else:
                    print("Order discard.")


        elif choice == "8":
            print("\n--- Order History ---")
            order_manager.list_orders()

            detail = input("View details of any order? (enter ID or press Enter to skip): ").strip()
            if detail:
                if detail.isdigit():
                    order_manager.show_order_details(int(detail))

                else:
                    print("Invalid order ID.")


        elif choice == "9":
            print("Exiting system...")
            break


        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")




        
if __name__=="__main__":
    main()