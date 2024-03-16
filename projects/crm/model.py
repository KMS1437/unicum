import json

class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class CRMSystem:
    def __init__(self):
        self.users = []

    def add_user(self, name, email, phone):
        user = User(name, email, phone)
        self.users.append(user)
        self.save_users_to_json()

    def delete_user(self, name):
        for user in self.users:
            if user.name == name:
                self.users.remove(user)
                self.save_users_to_json()
                break

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user

    def update_user(self, name, new_email, new_phone):
        user = self.find_user(name)
        if user:
            user.email = new_email
            user.phone = new_phone
            self.save_users_to_json()  # Save users to JSON file

    def save_users_to_json(self):
        user_list = []
        for user in self.users:
            user_dict = {
                "name": user.name,
                "email": user.email,
                "phone": user.phone
            }
            user_list.append(user_dict)
        with open("users.json", "w") as file:
            json.dump(user_list, file)
