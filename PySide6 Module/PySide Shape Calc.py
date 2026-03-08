from PySide6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QWidget, QRadioButton, QGroupBox, QLineEdit, QFormLayout, QStackedWidget
)
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class InputWidget(QWidget):
    def __init__(self, fields):  # fields: list of tuples (label, QLineEdit)
        super().__init__()
        self.inputs = {}
        layout = QFormLayout()
        for label in fields:
            edit = QLineEdit()
            self.inputs[label] = edit
            layout.addRow(label + ":", edit)
        self.setLayout(layout)

    def get_values(self):
        # Return dictionary {label: float_value}
        try:
            return {label: float(edit.text()) for label, edit in self.inputs.items()}
        except ValueError:
            return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ryuu's Shape Calculator (refactored)")

        # --- Shape Selection ---
        self.rectangle_radio = QRadioButton("Rectangle")
        self.circle_radio = QRadioButton("Circle")
        self.triangle_radio = QRadioButton("Triangle")
        self.rectangle_radio.setChecked(True)
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.rectangle_radio)
        radio_layout.addWidget(self.circle_radio)
        radio_layout.addWidget(self.triangle_radio)
        self.shape_select_group = QGroupBox("Shape")
        self.shape_select_group.setLayout(radio_layout)

        # --- Inputs Widgets ---
        self.rect_inputs = InputWidget(["Width", "Height"])
        self.circle_inputs = InputWidget(["Radius"])
        self.triangle_inputs = InputWidget(["Side 1", "Side 2", "Side 3"])

        self.stacked_inputs = QStackedWidget()
        self.stacked_inputs.addWidget(self.rect_inputs)     # index 0
        self.stacked_inputs.addWidget(self.circle_inputs)   # index 1
        self.stacked_inputs.addWidget(self.triangle_inputs) # index 2

        # --- Calculate Button & Result ---
        self.calculate_button = QPushButton("Calculate")
        self.result_label = QLabel()

        # --- Main Layout ---
        central = QWidget()
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.shape_select_group)
        top_layout.addWidget(self.stacked_inputs)
        layout.addLayout(top_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        central.setLayout(layout)
        self.setCentralWidget(central)

        # --- Signals ---
        self.rectangle_radio.toggled.connect(self.update_inputs)
        self.circle_radio.toggled.connect(self.update_inputs)
        self.triangle_radio.toggled.connect(self.update_inputs)
        self.calculate_button.clicked.connect(self.on_calculate)

        self.update_inputs()

    def update_inputs(self):
        if self.rectangle_radio.isChecked():
            self.stacked_inputs.setCurrentIndex(0)
        elif self.circle_radio.isChecked():
            self.stacked_inputs.setCurrentIndex(1)
        elif self.triangle_radio.isChecked():
            self.stacked_inputs.setCurrentIndex(2)

    def on_calculate(self):
        if self.rectangle_radio.isChecked():
            vals = self.rect_inputs.get_values()
            if vals:
                shape = Rectangle(vals["Width"], vals["Height"])
            else:
                self.result_label.setText("Invalid input!")
                return
        elif self.circle_radio.isChecked():
            vals = self.circle_inputs.get_values()
            if vals:
                shape = Circle(vals["Radius"])
            else:
                self.result_label.setText("Invalid input!")
                return
        elif self.triangle_radio.isChecked():
            vals = self.triangle_inputs.get_values()
            if vals:
                shape = Triangle(vals["Side 1"], vals["Side 2"], vals["Side 3"])
            else:
                self.result_label.setText("Invalid input!")
                return
        try:
            area = shape.area()
            peri = shape.perimeter()
            self.result_label.setText(f"Area: {area:.2f}   Perimeter: {peri:.2f}")
        except Exception as e:
            self.result_label.setText("Invalid values for calculation")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()