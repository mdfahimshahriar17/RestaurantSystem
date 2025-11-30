import json
import os


class User:
    def __init__(self, username, password, role="cashier"):
        self.username = username
        self.password = password #later: hashing
        self.role = role


    def to_dict(self):
        return{
            "username": self.username,
            "password": self.password,
            "role": self.role,
        }

    

class UserManager:
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), "users.json")
        self.users = []
        self.load_users()

    def load_users(self):
        """Read users.json and load into self.users"""
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.users = [User(**user_data) for user_data in data]
        
        except:
            self.users = []

    def save_users(self):
        """Save current users list into users.json"""
        data =[user.to_dict() for user in self.users]
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def register_user(self, username, password, role="cashier"):
        # Check duplicate username
        for u in self.users:
            if u.username == username:
                print("Username already exists!")
                return
            

        user = User(username, password, role)
        self.users.append(user)
        self.save_users()
        print(f"[User '{username}' registered successfully!]")


    def list_users(self):
        if not self.users:
            print("No users found")
            return

        print("\nRegistered Users:")
        for u in self.users:
            print(f"- {u.username} ({u.role})")
                