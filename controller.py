from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from accounts import Account, SavingAccount
from file_handler import save_account, load_account


class BankController(QMainWindow):
    """Controls the bank account GUI."""

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("bank_account.ui", self)

        self.account = None
        self.account_type = "None"
# AI used for Signal/Slot syntax and UI State Management.
        self.createAccountButton.clicked.connect(self.create_account)
        self.depositButton.clicked.connect(self.deposit_money)
        self.withdrawButton.clicked.connect(self.withdraw_money)
        self.showBalanceButton.clicked.connect(self.show_balance)
        self.saveButton.clicked.connect(self.save_account_data)
        self.loadButton.clicked.connect(self.load_account_data)
        self.clearButton.clicked.connect(self.clear_fields)

    def create_account(self) -> None:
        """Create a new account."""
        name = self.nameInput.text().strip()
        account_type = self.accountTypeCombo.currentText()
        balance_text = self.startBalanceInput.text().strip()

        if name == "":
            self.messageLabel.setText("Account name cannot be empty.")
            return

        if account_type == "None":
            self.messageLabel.setText("Please select an account type.")
            return

        try:
            balance = float(balance_text)
        except ValueError:
            self.messageLabel.setText("Starting balance must be a number.")
            return

        if balance < 0:
            self.messageLabel.setText("Starting balance cannot be negative.")
            return

        self.account_type = account_type

        if account_type == "Savings Account":
            self.account = SavingAccount(name)
            self.account.set_balance(balance)
        else:
            self.account = Account(name, balance)

        self.update_summary()
        self.messageLabel.setText("Account created.")

    def deposit_money(self) -> None:
        """Deposit money into the account."""
        if self.account is None:
            self.messageLabel.setText("Create an account first.")
            return

        try:
            amount = float(self.amountInput.text())
        except ValueError:
            self.messageLabel.setText("Amount must be a number.")
            return

        if self.account.deposit(amount):
            self.update_summary()
            self.messageLabel.setText("Deposit successful.")
        else:
            self.messageLabel.setText("Deposit must be greater than 0.")

    def withdraw_money(self) -> None:
        """Withdraw money from the account."""
        if self.account is None:
            self.messageLabel.setText("Create an account first.")
            return

        try:
            amount = float(self.amountInput.text())
        except ValueError:
            self.messageLabel.setText("Amount must be a number.")
            return

        if self.account.withdraw(amount):
            self.update_summary()
            self.messageLabel.setText("Withdrawal successful.")
        else:
            self.messageLabel.setText("Withdrawal cannot be completed.")

    def show_balance(self) -> None:
        """Show the current balance."""
        if self.account is None:
            self.messageLabel.setText("Create an account first.")
            return

        self.messageLabel.setText(f"Current balance: ${self.account.get_balance():.2f}")

    def save_account_data(self) -> None:
        """Save the current account to a CSV file."""
        if self.account is None:
            self.messageLabel.setText("Create an account before saving.")
            return

        save_account(
            "account_data.csv",
            self.account.get_name(),
            self.account_type,
            self.account.get_balance(),
            self.account.get_deposit_count()
        )

        self.messageLabel.setText("Account saved.")

    def load_account_data(self) -> None:
        """Load an account from the CSV file by name."""
        name = self.nameInput.text().strip()

        if name == "":
            self.messageLabel.setText("Enter an account name to load.")
            return

        data = load_account("account_data.csv", name)

        if data is None:
            self.messageLabel.setText("Account not found.")
            return

        self.account_type = data["account_type"]
        balance = float(data["balance"])
        deposit_count = int(data["deposit_count"])

        if self.account_type == "Savings Account":
            self.account = SavingAccount(data["name"])
            self.account.set_balance(balance)
            self.account.set_deposit_count(deposit_count)
        else:
# AI used for Signal/Slot syntax and UI State Management.            
            self.account = Account(data["name"], balance)

        self.nameInput.setText(data["name"])
        self.startBalanceInput.setText(str(balance))
        self.accountTypeCombo.setCurrentText(self.account_type)

        self.update_summary()
        self.messageLabel.setText("Account loaded.")

    def update_summary(self) -> None:
        """Update the account summary labels."""
        self.currentNameLabel.setText(f"Current Name: {self.account.get_name()}")
        self.currentTypeLabel.setText(f"Account Type: {self.account_type}")
        self.currentBalanceLabel.setText(f"Balance: ${self.account.get_balance():.2f}")
        self.depositCountLabel.setText(
            f"Deposit Count: {self.account.get_deposit_count()}"
        )

    def clear_fields(self) -> None:
        """Clear the input fields."""
        self.nameInput.clear()
        self.startBalanceInput.clear()
        self.amountInput.clear()
        self.accountTypeCombo.setCurrentIndex(0)

        self.currentNameLabel.setText("Current Name: None")
        self.currentTypeLabel.setText("Account Type: None")
        self.currentBalanceLabel.setText("Balance: $0.00")
        self.depositCountLabel.setText("Deposit Count: 0")
        self.messageLabel.setText("Cleared.")

        self.account = None
        self.account_type = "None"
