#Initializes the database, sets up the GUI, and starts the application

from gui import AccountGUI
from database import initialize_db
import tkinter as tk

def main():
    """
    Main function to initialize the database and start the GUI.
    """
    # Initialize the database
    initialize_db()

    # Create the main window
    root = tk.Tk()

    # Set up the GUI
    app = AccountGUI(root)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
