#Implements the GUI using Tkinter for interactions between user and database

import tkinter as tk
from account import Account, SavingAccount
from database import save_account, load_account, delete_account
from exceptions import AccountNotFoundException, InsufficientFundsException, InvalidAmountException

class AccountGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Account Manager")

        self.name_label = tk.Label(master, text="Account Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.balance_label = tk.Label(master, text="Amount:")
        self.balance_label.grid(row=1, column=0)
        self.balance_entry = tk.Entry(master)
        self.balance_entry.grid(row=1, column=1)

        self.message_label = tk.Label(master, text="", fg="red")
        self.message_label.grid(row=2, column=0, columnspan=2)

        self.create_button = tk.Button(master, text="Create Account", command=self.create_account)
        self.create_button.grid(row=3, column=0)

        self.deposit_button = tk.Button(master, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=3, column=1)

        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=4, column=0)

        self.balance_button = tk.Button(master, text="Check Balance", command=self.check_balance)
        self.balance_button.grid(row=4, column=1)

        self.delete_button = tk.Button(master, text="Delete Account", command=self.delete_account)
        self.delete_button.grid(row=5, column=0, columnspan=2)

    def create_account(self):
        """
        Create a new account and save it to the database.
        """
        name = self.name_entry.get()
        balance = float(self.balance_entry.get())
        account_type = SavingAccount if balance >= SavingAccount.MINIMUM else Account
        account = account_type(name, balance)
        save_account(account)
        self.message_label.config(text=f"Account for {name} created with balance {balance:.2f}.")

    def deposit(self):
        """
        Deposit money into an account.
        """
        name = self.name_entry.get()
        amount = float(self.balance_entry.get())
        try:
            account = load_account(name)
            account.deposit(amount)
            save_account(account)
            self.message_label.config(text=f"Deposited {amount:.2f} to {name}'s account.")
        except (AccountNotFoundException, InvalidAmountException) as e:
            self.message_label.config(text=str(e))

    def withdraw(self):
        """
        Withdraw money from an account.
        """
        name = self.name_entry.get()
        amount = float(self.balance_entry.get())
        try:
            account = load_account(name)
            account.withdraw(amount)
            save_account(account)
            self.message_label.config(text=f"Withdrew {amount:.2f} from {name}'s account.")
        except (AccountNotFoundException, InsufficientFundsException, InvalidAmountException) as e:
            self.message_label.config(text=str(e))

    def check_balance(self):
        """
        Check the balance of an account.
        """
        name = self.name_entry.get()
        try:
            account = load_account(name)
            self.message_label.config(text=f"Balance for {name} is {account.get_balance():.2f}")
        except AccountNotFoundException as e:
            self.message_label.config(text=str(e))

    def delete_account(self):
        """
        Delete an account from the database.
        """
        name = self.name_entry.get()
        try:
            delete_account(name)
            self.message_label.config(text=f"Deleted account for {name}.")
        except AccountNotFoundException as e:
            self.message_label.config(text=str(e))
