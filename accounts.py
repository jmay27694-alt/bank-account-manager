class Account:
    """Represents a regular bank account."""
# AI used for Type Hinting and Polymorphism syntax.
    def __init__(self, name: str, balance: float = 0) -> None:
        self.__account_name = name
        self.__account_balance = balance
        self.set_balance(self.__account_balance)

    def deposit(self, amount: float) -> bool:
        """Deposit money into the account."""
        if amount <= 0:
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account."""
        if amount <= 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self) -> float:
        """Return the account balance."""
        return self.__account_balance

    def get_name(self) -> str:
        """Return the account name."""
        return self.__account_name

    def set_balance(self, value: float) -> None:
        """Set the account balance."""
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value

    def set_name(self, value: str) -> None:
        """Set the account name."""
        self.__account_name = value

    def get_deposit_count(self) -> int:
        """Return deposit count for regular accounts."""
        return 0


class SavingAccount(Account):
    """Represents a savings account."""

    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name: str) -> None:
        super().__init__(name, SavingAccount.MINIMUM)
        self.__deposit_count = 0

    def get_deposit_count(self) -> int:
        """Return the number of deposits."""
        return self.__deposit_count

    def set_deposit_count(self, count: int) -> None:
        """Set the number of deposits."""
        self.__deposit_count = count

    def apply_interest(self) -> None:
        """Apply interest to the savings account."""
        interest = self.get_balance() * SavingAccount.RATE
        self.set_balance(self.get_balance() + interest)

    def deposit(self, amount: float) -> bool:
        """Deposit money and apply interest every 5 deposits."""
        if amount <= 0:
            return False
# AI used for Type Hinting and Polymorphism syntax.            
        result = super().deposit(amount)

        if result:
            self.__deposit_count += 1
            if self.__deposit_count % 5 == 0:
                self.apply_interest()

        return result

    def withdraw(self, amount: float) -> bool:
        """Withdraw money without going below the minimum balance."""
        if amount <= 0:
            return False

        if self.get_balance() - amount < SavingAccount.MINIMUM:
            return False

        return super().withdraw(amount)

    def set_balance(self, value: float) -> None:
        """Set savings balance without going below the minimum."""
        if value < SavingAccount.MINIMUM:
            super().set_balance(SavingAccount.MINIMUM)
        else:
            super().set_balance(value)