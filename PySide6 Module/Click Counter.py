import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QVBoxLayout

class CounterModel:
    def __init__(self):
        super().__init__()
        self._count = 0
        
    def increment(self):
        self._count += 1
            
    def reset(self):
        self._count = 0
            
    @property
    def count(self):
            return self._count
        
    def display_text(self):
        if self._count == 0:
            return "You haven't clicked the button yet."
        return f"You have clicked the button {self._count} times."

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ryuu's Click Counter")
        
        self.model = CounterModel()
        
        self.label = QLabel("You haven't clicked the button yet.")
        self.click_button = QPushButton("Click me!")
        self.reset_button = QPushButton("Reset")
        
        container = QWidget()
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.click_button)
        v_layout.addWidget(self.reset_button)
        v_layout.addWidget(self.label)
        container.setLayout(v_layout)
        self.setCentralWidget(container)
        
        self.click_button.clicked.connect(self.handle_button_press)
        self.reset_button.clicked.connect(self.handle_reset_button_press)
        
    def handle_button_press(self):
        self.model.increment()
        self.update_label()
    
    def handle_reset_button_press(self):
        self.model.reset()
        self.update_label()
        
    def update_label(self):
        self.label.setText(self.model.display_text())
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()