import sys
from PyQt6.QtWidgets import QApplication
from controller import BankController


def main() -> None:
    """Run the bank account app."""
    app = QApplication(sys.argv)
    window = BankController()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()