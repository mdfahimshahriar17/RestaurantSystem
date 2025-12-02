from users.user import UserManager
from menu.menu_manager import MenuManager
from menu.pizza import Pizza
from menu.burger import Burger
from menu.drink import Drink


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
    print("7. Exit")



def main():
    user_manager = UserManager()
    menu_manager = MenuManager()
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



        elif choice == "7":
            print("Exiting system...")
            break


        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")

        
if __name__=="__main__":
    main()