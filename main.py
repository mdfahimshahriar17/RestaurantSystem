from users.user import UserManager

def main_menu(current_user):
    print("==== Restaurant Management System ====")


    if current_user:
        print(f"Logged in as: {current_user.username} ({current_user.role})")
    else:
        print("Not logged in.")


    print("1. Register User")
    print("2. Login")
    print("3. List Users")
    print("4. Exit")


def main():
    user_manager = UserManager()
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
            print("Existing system...")
            break

        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")


if __name__=="__main__":
    main()