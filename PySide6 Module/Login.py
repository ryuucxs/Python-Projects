import json
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout

def log(func):
    def wrapper(*args, **kwargs):
        log = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} called")
        return log
    return wrapper

class Model:
    def __init__(self, view):
        self.view = view
        self.login_data = {}
        self.filename = "TaskManagerLogin.json"
        
    @log
    def save_user(self, username, password):
        self.login_data[username] = password
        with open(self.filename, "w") as file:
            json.dump(self.login_data, file)
            return self.login_data[username] == password

    @log
    def create_admin_login(self):
        admin_username = "admin"
        admin_password = "admin104"
        self.login_data["Admin Login"] = [admin_username, admin_password]
        with open(self.filename, "w") as file:
            json.dump(self.login_data, file)
            return self.login_data["Admin Login"]
        
    @log       
    def load_user(self):
        with open(self.filename, "r") as file:
            self.login_data = json.load(file)
            return self.login_data
    
    @log
    def sign_up_button(self, username, password):
        self.save_user(username, password)
        if not username or not password:
            return "Please enter a username and password"
        self.save_user(username, password)
        return username, password, "User created successfully"
    
    @log
    def login_button(self, username, password):
        self.load_user()
        if "User Login" not in self.login_data:
            return "No user found. Please sign up first."
        stored_username, stored_password = self.login_data["User Login"]
        if username == stored_username and password == stored_password:
            return username, password, "Login successful"
        else:
            return "Invalid username or password"
        
    @log
    def admin_login_button(self, username, password):
        self.load_user()
        if "Admin Login" not in self.login_data:
            return "Admin login not found. Please create an admin login first."
        stored_username, stored_password = self.login_data["Admin Login"]
        if username == stored_username and password == stored_password:
            return username, password, "Admin login successful"
        else:
            return "Invalid admin username or password"
        
    @log
    def reset_inputs(self):
        self.view.username_input.clear()
        self.view.password_input.clear()
        

class AdminView(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Admin Preview")
        
        
        
        
class View(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label_n = QLabel("Enter your username:")
        self.label_p = QLabel("Enter your password:")
        self.label_validation = QLabel("")
        
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        
        self.button_signup = QPushButton("Signup")
        self.button_login = QPushButton("Login")
        self.button_admin = QPushButton("Admin Login")
        
        self.setWindowTitle("Ryuu's Login Window")
        
        container = QWidget()
        
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.label_n)
        layout_vertical.addWidget(self.username_input)
        layout_vertical.addWidget(self.label_p)
        layout_vertical.addWidget(self.password_input)
        layout_vertical.addWidget(self.label_validation)
        
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.button_signup)
        layout_horizontal.addWidget(self.button_login)
        layout_horizontal.addWidget(self.button_admin)
        
        layout_vertical.addLayout(layout_horizontal)

        container.setLayout(layout_vertical)
        self.setLayout(layout_vertical)
            
class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model(view)
        self.model.create_admin_login()
        self.setup_connections()

    def setup_connections(self):
        self.view.button_signup.clicked.connect(self.handle_signup)
        self.view.button_login.clicked.connect(self.handle_login)
        self.view.button_admin.clicked.connect(self.handle_admin_login)

    def handle_signup(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        result = self.model.sign_up_button(username, password)
        if isinstance(result, tuple):
            self.view.label_validation.setText(result[2])
        else:
            self.view.label_validation.setText(result)

    def handle_login(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        result = self.model.login_button(username, password)
        if isinstance(result, tuple):
            self.view.label_validation.setText(result[2])
        else:
            self.view.label_validation.setText(result)

    def handle_admin_login(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        result = self.model.admin_login_button(username, password)
        if isinstance(result, tuple):
            self.view.label_validation.setText(result[2])
        else:
            self.view.label_validation.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = View()
    controller = Controller(view)
    view.show()
    sys.exit(app.exec())
