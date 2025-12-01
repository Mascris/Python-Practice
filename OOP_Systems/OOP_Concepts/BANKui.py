from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QInputDialog, QMessageBox, QComboBox, QFrame,
    QScrollArea, QTextEdit
)
from PyQt6.QtGui import QFont, QColor, QPalette, QIcon, QPixmap
from PyQt6.QtCore import Qt, QSize
import sys

# --- BankAccount Class (Business Logic) ---
class BankAccount:
    """
    Manages account data and operations.
    """
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = ["Account created."]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: ${amount:.2f}")
            return True
        return False

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.pin:
            return False, "Incorrect PIN."
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if self.balance < amount:
            return False, "Insufficient funds."
        
        self.balance -= amount
        self.history.append(f"Withdrew: ${amount:.2f}")
        return True, "Withdrawal successful."

    def get_balance_str(self):
        return f"${self.balance:,.2f}"

    def get_history(self):
        return "\n".join(reversed(self.history))

# --- Global Data ---
accounts = {
    "Lassa": BankAccount("Lassa", 3333, 1252),
    "Mopo": BankAccount("Mopo", 6666, 1500),
    "Luna": BankAccount("Luna",1234, 6000)
}

# --- Modern PyQt6 GUI ---
class ModernBankApp(QWidget):
    """
    The main application window.
    """
    def __init__(self):
        super().__init__()
        self.current_account = None
        self._init_ui()
        self._connect_signals()
        self.update_ui_for_selected_account()

    def _init_ui(self):
        """Initialize the UI components."""
        self.setWindowTitle("Apex Bank")
        self.setGeometry(100, 100, 600, 550)
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #E0E0E0;
                font-family: 'Segoe UI';
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)

        # --- Header ---
        header_layout = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap('logo.png').scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        
        title = QLabel("Apex Bank")
        title.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        title.setStyleSheet("color: #BB86FC;")

        header_layout.addWidget(logo_label)
        header_layout.addWidget(title)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)

        # --- Account Selection ---
        account_layout = QHBoxLayout()
        self.account_combo = QComboBox()
        self.account_combo.setFont(QFont("Segoe UI", 12))
        self.account_combo.addItems(accounts.keys())
        self.account_combo.setStyleSheet("""
            QComboBox {
                background-color: #1E1E1E;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 10px;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)
        
        self.add_account_btn = QPushButton(QIcon('add_user.png'), " Create Account")
        self.add_account_btn.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        self.add_account_btn.setIconSize(QSize(18,18))
        self.add_account_btn.setStyleSheet("""
            QPushButton {
                background-color: #03DAC5; color: #121212; 
                padding: 10px; border-radius: 8px;
            }
            QPushButton:hover { background-color: #018786; }
        """)

        account_layout.addWidget(self.account_combo)
        account_layout.addWidget(self.add_account_btn)
        main_layout.addLayout(account_layout)
        
        # --- Balance Display ---
        self.balance_frame = QFrame()
        self.balance_frame.setStyleSheet("""
            QFrame {
                background-color: #1E1E1E;
                border-radius: 15px;
                border: 1px solid #333;
            }
        """)
        balance_frame_layout = QVBoxLayout(self.balance_frame)
        
        balance_title = QLabel("CURRENT BALANCE")
        balance_title.setFont(QFont("Segoe UI", 10))
        balance_title.setStyleSheet("color: #B0B0B0;")
        
        self.balance_label = QLabel("$0.00")
        self.balance_label.setFont(QFont("Segoe UI", 36, QFont.Weight.Bold))

        balance_frame_layout.addWidget(balance_title)
        balance_frame_layout.addWidget(self.balance_label)
        main_layout.addWidget(self.balance_frame)

        # --- Action Buttons ---
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)
        
        self.deposit_btn = self._create_action_button('deposit.png', "Deposit")
        self.withdraw_btn = self._create_action_button('withdraw.png', "Withdraw")

        buttons_layout.addWidget(self.deposit_btn)
        buttons_layout.addWidget(self.withdraw_btn)
        main_layout.addLayout(buttons_layout)

        # --- Transaction History ---
        history_label = QLabel("Transaction History")
        history_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        
        self.history_view = QTextEdit()
        self.history_view.setReadOnly(True)
        self.history_view.setFont(QFont("Courier New", 10))
        self.history_view.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        
        main_layout.addWidget(history_label)
        main_layout.addWidget(self.history_view)

    def _create_action_button(self, icon_path, text):
        """Helper to create styled buttons."""
        button = QPushButton(QIcon(icon_path), f" {text}")
        button.setIconSize(QSize(24, 24))
        button.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        button.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                border-radius: 8px;
                padding: 15px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #444444;
            }
        """)
        return button

    def _connect_signals(self):
        """Connect widget signals to slots."""
        self.account_combo.currentTextChanged.connect(self.update_ui_for_selected_account)
        self.deposit_btn.clicked.connect(self.deposit)
        self.withdraw_btn.clicked.connect(self.withdraw)
        self.add_account_btn.clicked.connect(self.create_account)

    def update_ui_for_selected_account(self):
        """Updates the UI with the current account's data."""
        account_name = self.account_combo.currentText()
        if account_name:
            self.current_account = accounts[account_name]
            self.balance_label.setText(self.current_account.get_balance_str())
            self.history_view.setText(self.current_account.get_history())
        else:
            self.balance_label.setText("$0.00")
            self.history_view.setText("No account selected.")
            
    def _show_message(self, title, text, icon=QMessageBox.Icon.Information):
        """Displays a styled message box."""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(icon)
        msg_box.setStyleSheet("""
            QMessageBox { background-color: #1E1E1E; }
            QLabel { color: #E0E0E0; }
            QPushButton { background-color: #BB86FC; color: #121212; padding: 5px 15px; border-radius: 5px; }
        """)
        msg_box.exec()

    # --- Actions ---
    def deposit(self):
        if not self.current_account: return
        
        amount, ok = QInputDialog.getInt(self, "Deposit", "Enter amount:", min=1)
        if ok and self.current_account.deposit(amount):
            self.update_ui_for_selected_account()
            self._show_message("Success", f"Successfully deposited ${amount:.2f}.")
        elif ok:
            self._show_message("Error", "Invalid deposit amount.", QMessageBox.Icon.Warning)

    def withdraw(self):
        if not self.current_account: return

        pin, ok_pin = QInputDialog.getInt(self, "Security Check", "Enter PIN:",-1, 0)
        if not ok_pin: return
        
        amount, ok_amount = QInputDialog.getInt(self, "Withdraw", "Enter amount:", min=1)
        if not ok_amount: return

        success, message = self.current_account.withdraw(amount, pin)
        if success:
            self.update_ui_for_selected_account()
            self._show_message("Success", message)
        else:
            self._show_message("Withdrawal Failed", message, QMessageBox.Icon.Critical)
            
    def create_account(self):
        name, ok_name = QInputDialog.getText(self, "Create Account", "Enter new account name:")
        if not (ok_name and name):
            return
        if name in accounts:
            self._show_message("Error", "Account with this name already exists.", QMessageBox.Icon.Warning)
            return

        pin, ok_pin = QInputDialog.getInt(self, "Create PIN", "Enter a 4-digit PIN:", min=1000, max=9999)
        if not ok_pin:
            return
            
        accounts[name] = BankAccount(name, pin)
        self.account_combo.addItem(name)
        self.account_combo.setCurrentText(name)
        self._show_message("Success", f"Account '{name}' created successfully!")


# --- Run Application ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # You will need to create these icon files or remove them for the code to run
    # For example, you can find free icons from websites like Flaticon or Font Awesome
    # and save them as 'logo.png', 'add_user.png', 'deposit.png', 'withdraw.png' 
    # in the same directory as your script.
    window = ModernBankApp()
    window.show()
    sys.exit(app.exec())
