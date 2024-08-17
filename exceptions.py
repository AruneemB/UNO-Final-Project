#Custom exceptions for implementation in the Account and SavingAccount classes

class AccountNotFoundException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class InvalidAmountException(Exception):
    pass
