import sys
import operator
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
)


def safe_divide(a, b):
    if b == 0:
        return "Error"
    return a / b


class CalculatorUI(QMainWindow):
    """Dark-themed calculator with full arithmetic logic."""

    OPERATIONS = {
        "÷": safe_divide,
        "×": operator.mul,
        "−": operator.sub,
        "+": operator.add,
    }

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ryuu's Calculator")
        self.setFixedSize(420, 640)

        # Calculator state
        self.first_number = None
        self.current_operator = None
        self.reset_on_next_digit = False

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(12)

        # Top area: small expression label + big display
        self.expr_label = QLabel("")
        self.expr_label.setObjectName("expr")
        self.expr_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.display = QLineEdit("")
        self.display.setObjectName("display")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        main_layout.addWidget(self.expr_label)
        main_layout.addWidget(self.display)

        # Button grid area
        buttons_widget = QWidget()
        buttons_layout = QGridLayout(buttons_widget)
        buttons_layout.setSpacing(12)
        buttons_layout.setContentsMargins(6, 6, 6, 6)

        # Layout pattern matching the screenshot
        # Each inner list: (label, role)
        grid = [
            [('C',  'normal'), ('±', 'normal'), ('⌫', 'normal'), ('÷', 'op')],
            [('7',  'normal'), ('8', 'normal'), ('9', 'normal'), ('×', 'op')],
            [('4',  'normal'), ('5', 'normal'), ('6', 'normal'), ('−', 'op')],
            [('1',  'normal'), ('2', 'normal'), ('3', 'normal'), ('+', 'op')],
            [('0',  'normal'), ('.', 'normal'), ('=', 'equal')],
        ]

        # Create buttons and add to grid
        self.buttons = {}
        for r, row in enumerate(grid):
            for c, (text, role) in enumerate(row):
                btn = QPushButton(text)
                btn.setObjectName('btn')
                btn.setProperty('role', role)
                self.buttons[text] = btn
                # Make = span 2 columns
                if text == '=':
                    buttons_layout.addWidget(btn, r, c, 1, 2)
                else:
                    buttons_layout.addWidget(btn, r, c)

        # Connect signals
        self.connect_signals()

        main_layout.addWidget(buttons_widget)

        # lower spacing area to mimic card shadow
        footer = QWidget()
        footer.setFixedHeight(6)
        main_layout.addWidget(footer)

        self.apply_styles()

    # ── Signal Connections ──────────────────────────────────────

    def connect_signals(self):
        # Number buttons
        for key in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            self.buttons[key].clicked.connect(self.number_pressed)

        # Decimal
        self.buttons['.'].clicked.connect(self.decimal_pressed)

        # Operators
        for key in ('÷', '×', '−', '+'):
            self.buttons[key].clicked.connect(self.operator_pressed)

        # Equal
        self.buttons['='].clicked.connect(self.equals_pressed)

        # Clear
        self.buttons['C'].clicked.connect(self.clear_pressed)

        # Negate
        self.buttons['±'].clicked.connect(self.negate_pressed)

        # Backspace
        self.buttons['⌫'].clicked.connect(self.backspace_pressed)

    # ── Slot Methods ───────────────────────────────────────────

    def number_pressed(self):
        digit = self.sender().text()
        if self.reset_on_next_digit:
            self.display.clear()
            self.reset_on_next_digit = False
        current = self.display.text()
        self.display.setText(current + digit)

    def decimal_pressed(self):
        current = self.display.text()
        if '.' not in current:
            self.display.setText(current + '.')

    def operator_pressed(self):
        op = self.sender().text()
        if self.display.text() == '' and self.first_number is None:
            return
        # If chaining operations, compute the intermediate result first
        if self.first_number is not None and self.current_operator and not self.reset_on_next_digit:
            self.equals_pressed()
        if self.display.text():
            self.first_number = float(self.display.text())
        self.current_operator = op
        self.expr_label.setText(f"{self.format_number(self.first_number)} {op}")
        self.reset_on_next_digit = True

    def equals_pressed(self):
        if self.first_number is None or self.current_operator is None:
            return
        if self.display.text() == '':
            return
        second = float(self.display.text())
        result = self.OPERATIONS[self.current_operator](self.first_number, second)
        if result == "Error":
            self.expr_label.setText("Error: Division by zero")
            self.display.clear()
            self.first_number = None
            self.current_operator = None
            return
        self.expr_label.setText(
            f"{self.format_number(self.first_number)} {self.current_operator} {self.format_number(second)} ="
        )
        self.display.setText(self.format_number(result))
        self.first_number = result
        self.current_operator = None
        self.reset_on_next_digit = True

    def clear_pressed(self):
        self.display.clear()
        self.expr_label.clear()
        self.first_number = None
        self.current_operator = None
        self.reset_on_next_digit = False

    def negate_pressed(self):
        current = self.display.text()
        if current and current != '0':
            if current.startswith('-'):
                self.display.setText(current[1:])
            else:
                self.display.setText('-' + current)

    def backspace_pressed(self):
        current = self.display.text()
        if current:
            self.display.setText(current[:-1])

    # ── Helpers ────────────────────────────────────────────────

    def format_number(self, value):
        """Display integers without .0 and floats normally."""
        if isinstance(value, float) and value == int(value):
            return str(int(value))
        return str(value)

    # ── Styles ─────────────────────────────────────────────────

    def apply_styles(self):
        # Overall dark window background
        self.setStyleSheet("""
        QMainWindow { background-color: #0f1114; }

        /* Expression label */
        QLabel#expr {
            color: #bfbfc6;
            font-size: 16px;
            padding-left: 8px;
        }

        /* Display */
        QLineEdit#display {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #1b1d20, stop:1 #111214);
            color: #e6e6e6;
            border: 1px solid #2b2d31;
            border-radius: 6px;
            padding: 20px;
            font-size: 48px;
            min-height: 86px;
        }

        /* Default button style */
        QPushButton[role="normal"] {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #22242a, stop:1 #18191c);
            color: #dcdce0;
            border: 1px solid #2f3136;
            border-radius: 8px;
            font-size: 22px;
            min-width: 74px;
            min-height: 64px;
        }
        QPushButton[role="normal"]:hover {
            background: #2b2d33;
        }

        /* Operator buttons (accent orange) */
        QPushButton[role="op"] {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #2b2b2b, stop:1 #1f1f1f);
            color: #f39c63;
            border: 1px solid #3b3b3b;
            border-radius: 8px;
            font-weight: 600;
            font-size: 22px;
            min-width: 74px;
            min-height: 64px;
        }
        QPushButton[role="op"]:hover {
            background: #2f2f2f;
        }

        /* Equal button - match size and shape of other buttons, but with accent */
        QPushButton[role="equal"] {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 #b86b3a, stop:1 #8c4f2a);
            color: white;
            border: 1px solid #7a4a2a;
            border-radius: 8px;
            font-size: 22px;
            font-weight: 700;
            min-width: 74px;
            min-height: 64px;
        }
        QPushButton[role="equal"]:hover {
            background: #d07b45;
        }
        """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CalculatorUI()
    w.show()
    sys.exit(app.exec())
