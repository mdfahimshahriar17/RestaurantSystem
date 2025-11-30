from users.user import UserManager

def main_menu():
    print("==== Restaurant Management System ====")
    print("1. Create Test User")
    print("2. Show Users")
    print("3. Exit")


def main():
    user_manager = UserManager()

    while True:
        main_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Role (admin/cashier): ").lower()
            user_manager.register_user(username, password, role)
        
        elif choice == "2":
            user_manager.list_users()

        elif choice == "3":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")


if __name__=="__main__":
    main()