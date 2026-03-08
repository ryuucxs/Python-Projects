import sys
from PySide6.QtWidgets import (
QApplication, 
QMainWindow, 
QWidget, 
QVBoxLayout, 
QHBoxLayout, 
QLabel, 
QPushButton, 
QListWidget, 
QLineEdit
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Ryuu's To Do List")
        
        self.label = QLabel("My To Do List")
        self.list = QListWidget()
        self.input = QLineEdit()
        
        self.button_add = QPushButton("Add Task")
        self.button_add.clicked.connect(lambda: self.manage_tasks("add"))
        
        self.button_edit = QPushButton("Edit Task")
        self.button_edit.clicked.connect(lambda: self.manage_tasks("edit"))
        
        self.button_remove = QPushButton("Remove Task")
        self.button_remove.clicked.connect(lambda: self.manage_tasks("remove"))
        
        container = QWidget()
        
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.label)
        layout_vertical.addWidget(self.input)
        layout_vertical.addWidget(self.list)        
        
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.button_add)
        layout_horizontal.addWidget(self.button_edit)
        layout_horizontal.addWidget(self.button_remove)
        
        layout_vertical.addLayout(layout_horizontal)
        
        container.setLayout(layout_vertical)
        self.setCentralWidget(container)
        
    def manage_tasks(self, action):
        
        task = self.input.text()
        if not task:
            return
        
        if action == "add":
            self.list.addItem(task)
            
        elif action == "edit":
            selected_items = self.list.selectedItems()
            if selected_items:
                selected_items[0].setText(task)
                
        elif action == "remove":
            selected_items = self.list.selectedItems()
            if selected_items:
                self.list.takeItem(self.list.row(selected_items[0]))
        
        self.input.clear()
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()