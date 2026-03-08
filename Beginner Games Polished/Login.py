import json
import os
from typing import Dict, Optional
import time


class Model:
    def __init__(self) -> None:
        self.user_data: Dict[str, list] = {}
        self.filename = "Login_Users.json"
        
    def create_admin_data(self) -> Optional[Dict[str, list]]:
        
        # Check if Admin Logins exist already
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                content = file.read().strip()
                if content:
                    self.user_data = json.loads(content)
                else:
                    self.user_data = {}
        
        # Check if "Admin Login" already exists
        if "Admin Login" not in self.user_data:
                    
            # Create "Admin Login Data"
            try:
                with open(self.filename, "w") as admin:
                    admin_username = "admin"
                    admin_password = "admin104"
                    self.user_data["Admin Login"] = [admin_username, admin_password]
                    json.dump(self.user_data, admin)
                return self.user_data
            except Exception:
                return None
            
    def create_user(self, username: str, password: str) -> Optional[Dict[str, list]]:
        
        # Check if file already exists otherwise create one
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                content = file.read().strip()
                if content:
                    self.user_data = json.loads(content)
                else:
                    self.user_data = {}
        else:
            self.user_data = {}
        
        # Check if "User Login" Dictionary exists, otherwise create it    
        if "User Login" not in self.user_data:
            self.user_data["User Login"] = []
        
        # Add User Login details    
        self.user_data["User Login"].append([username, password])
        
        # Save User Login details
        try:
            with open(self.filename, "w") as new_user:
                json.dump(self.user_data, new_user)
            return self.user_data
        except Exception:
            return None
        
    def check_user(self, username: str) -> Optional[str]:
        with open(self.filename, "r") as file:
            self.user_data = json.load(file)
        
        # Check each username in a loop
        for usernames in self.user_data.get("User Login", []):
            if usernames[0] == username:
                return username
        return None


class View:
    def __init__(self) -> None:
        pass
    
    def show_message(self, text: str) -> Optional[str]:
        print(text)

class Control:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()
                
    def sign_up(self) -> Optional[str]:
        while True:
            ask_username = input("What should your username be: ")
            if self.model.check_user(ask_username) != None:
                continue
            ask_password = input("What should your password be: ")
            self.model.create_user(ask_username, ask_password)
            return f"Succesfully created an account with\nUsername: {ask_username}, Password: {ask_password}"
        
    def login_as_user(self) -> Optional[str]:
        with open(self.model.filename, "r") as file:
            self.user_data = json.load(file)
        
        users = self.user_data.get("User Login", [])
        while True:
            ask_username = input("Enter Username: ").strip()
            ask_password = input("Enter Password: ").strip()

            # Check each entry for a match!
            for entry in users:
                if (
                    isinstance(entry, list) and
                    len(entry) == 2 and
                    entry[0] == ask_username and
                    entry[1] == ask_password
                ):
                    return "You're logged in as a User"
            print("Username or Password is wrong")
            ask = input("Do you want to go back to the Menu (yes/no): ").lower()
            if ask == "yes":
                break
            else:
                continue
                
    def login_as_admin(self) -> Optional[str]:
        with open(self.model.filename, "r") as file:
            self.user_data = json.load(file)
        
        admin_credentials = self.user_data.get("Admin Login", [])
        while True:    
            ask_username = input("Enter Username: ").strip()
            ask_password = input("Enter Password: ").strip()
            
            # Properly check admin credentials
            if (
                isinstance(admin_credentials, list) and
                len(admin_credentials) == 2 and
                ask_username == admin_credentials[0] and
                ask_password == admin_credentials[1]
            ):
                return "You're logged in as an Admin"
            else:
                print("Username or Password is wrong")
                ask = input("Do you want to go back to the Menu (yes/no): ").lower()
                if ask == "yes":
                    break
                else:
                    continue
        
    def start_login(self) -> None:
        self.view.show_message("Welcome to the Login Window\n"
                               " ")
        self.model.create_admin_data()
        while True:
            time.sleep(1)
            self.view.show_message("Write the number of the action you want to follow:\n"
                                "1. Sign up and create an account\n"
                                "2. Login on an existing account\n"
                                "3. Login as an Admin\n"
                                "4. Exit the Program")
            time.sleep(1)
            ask_action = input("Choose your action: ").strip()
            if ask_action.isdigit() is True:
                
                # Create an account
                if ask_action == "1":
                    result = self.sign_up()
                    if result is not None:
                        self.view.show_message(result)
                        
                # Login to an existing account
                elif ask_action == "2":
                    result = self.login_as_user()
                    if result is not None:
                        self.view.show_message(result)
                
                # Login to admin account        
                elif ask_action == "3":
                    result = self.login_as_admin()
                    if result is not None:
                        self.view.show_message(result)
                
                # Exit the program
                elif ask_action == "4":
                    break
                    
                else:
                    self.view.show_message("Enter a proper action")
                    
            else:
                self.view.show_message("Enter only numeric numbers as actions")


if __name__ == "__main__":
    c = Control()
    c.start_login()
