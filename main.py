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
            # test user create korar jonno just ekta dummy call
            user_manager.register_user("admin", "1234", "admin")
        
        elif choice == "2":
            user_manager.list_users()

        elif choice == "3":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice! please try again")

        input("\nPress Enter to continue...")


if __name__=="__main__":
    main()