class User:
    def __init__(self, username, password, role="cashier"):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User(username='{self.username}', role='{self.role}')"
    

class UserManager:
    def __init__(self):
        #future e file thakle load korbo
        self.users = []

    def register_user(self, username, password, role="cashier"):
        user = User(username, password, role)
        self.users.append(user)
        print(f"[OK] User created: {user}")

    def list_users(self):
        if not self.users:
            print("No users found")

        else:
            for user in self.users:
                print(user)
                