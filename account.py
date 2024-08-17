#Contains Account and SavingAccount classes
#Improvements made with data validation, exception handling, and modifications of the original functionalities

class Account:
    def __init__(self, name: str, balance: float = 0):
        self.__account_name = name
        self.__account_balance = balance
        self.set_balance(balance)

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            raise InvalidAmountException("Deposit amount must be positive.")
        self.__account_balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise InvalidAmountException("Withdrawal amount must be positive.")
        if amount > self.__account_balance:
            raise InsufficientFundsException("Insufficient funds for withdrawal.")
        self.__account_balance -= amount
        return True

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name

    def set_balance(self, balance: float) -> None:
        if balance < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = balance

    def set_name(self, value: str) -> None:
        self.__account_name = value

    def __str__(self) -> str:
        return f'Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}'


class SavingAccount(Account):
    MINIMUM = 100
    RATE = 0.02

    def __init__(self, name: str, balance: float = 0):
        super().__init__(name, balance)
        self.__account_balance = self.MINIMUM
        self.__deposit_count = 0

    def apply_interest(self) -> None:
        if self.__deposit_count % 5 == 0:
            self.__account_balance += self.RATE * self.__account_balance

    def deposit(self, amount: float) -> bool:
        deposit_status = super().deposit(amount)
        if deposit_status:
            self.__deposit_count += 1
            self.apply_interest()
        return deposit_status

    def withdraw(self, amount: float) -> bool:
        if self.__account_balance - amount < self.MINIMUM:
            raise InsufficientFundsException("Cannot withdraw below the minimum balance.")
        return super().withdraw(amount)

    def __str__(self) -> str:
        return f'SAVING ACCOUNT: {super().__str__()}'
