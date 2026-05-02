class Account:

    def __init__(self, name, balance=0):
        self.account_name = name
        self.account_balance = balance
        self.set_balance(self.account_balance)

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.account_balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name

    def set_balance(self, value):
        if value < 0:
            self.account_balance = 0
        else:
            self.account_balance = value

    def set_name(self, value):
        self.account_name = value

    def get_deposit_count(self):
        return 0


class SavingAccount(Account):

    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name):
        super().__init__(name, SavingAccount.MINIMUM)
        self.deposit_count = 0

    def get_deposit_count(self):
        return self.deposit_count

    def set_deposit_count(self, count):
        self.deposit_count = count

    def apply_interest(self):
        interest = self.get_balance() * SavingAccount.RATE
        self.set_balance(self.get_balance() + interest)

    def deposit(self, amount):
        if amount <= 0:
            return False
        result = super().deposit(amount)
        if result:
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.apply_interest()
        return result

    def withdraw(self, amount):
        if amount <= 0:
            return False
        if self.get_balance() - amount < SavingAccount.MINIMUM:
            return False
        return super().withdraw(amount)

    def set_balance(self, value):
        if value < SavingAccount.MINIMUM:
            super().set_balance(SavingAccount.MINIMUM)
        else:
            super().set_balance(value)
