#Handles interactions with SQLite database for storing and retrieving account information

import sqlite3
from account import Account, SavingAccount

DATABASE = "accounts.db"

def initialize_db():
    """
    Initialize the SQLite database and create the accounts table if it doesn't exist.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                name TEXT PRIMARY KEY,
                balance REAL,
                is_saving INTEGER
            )
        """)
        conn.commit()

def save_account(account: Account) -> None:
    """
    Save or update an account in the database.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO accounts (name, balance, is_saving)
            VALUES (?, ?, ?)
        """, (account.get_name(), account.get_balance(), isinstance(account, SavingAccount)))
        conn.commit()

def load_account(name: str) -> Account:
    """
    Load an account from the database by name.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, balance, is_saving FROM accounts WHERE name = ?", (name,))
        row = cursor.fetchone()
        if row is None:
            raise AccountNotFoundException(f"No account found for {name}.")
        if row[2]:
            return SavingAccount(row[0], row[1])
        else:
            return Account(row[0], row[1])

def delete_account(name: str) -> None:
    """
    Delete an account from the database by name.
    """
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM accounts WHERE name = ?", (name,))
        if cursor.rowcount == 0:
            raise AccountNotFoundException(f"No account found for {name}.")
        conn.commit()
