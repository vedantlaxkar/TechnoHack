from tkinter import *

# Sample ATM Class
class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def check_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Your new balance is ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn ${amount}. Your new balance is ${self.balance}"
        else:
            return "Insufficient funds"

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            return "PIN changed successfully"
        else:
            return "Incorrect PIN"

# Global ATM Object
atm = ATM(1000, "1234")

# Functions for Main Page
def goto_check_balance():
    clear_screen()
    check_balance_frame.pack(padx=10, pady=10)

def goto_deposit():
    clear_screen()
    deposit_frame.pack(padx=10, pady=10)

def goto_withdraw():
    clear_screen()
    withdraw_frame.pack(padx=10, pady=10)

def goto_change_pin():
    clear_screen()
    change_pin_frame.pack(padx=10, pady=10)

def clear_screen():
    for frame in [check_balance_frame, deposit_frame, withdraw_frame, change_pin_frame]:
        frame.pack_forget()

# Functions for Check Balance
def handle_check_balance():
    result_label.config(text=atm.check_balance())

# Functions for Deposit
def handle_deposit():
    try:
        amount = float(deposit_amount_entry.get())
        result_label.config(text=atm.deposit(amount))
    except ValueError:
        result_label.config(text="Please enter a valid amount.")

# Functions for Withdraw
def handle_withdraw():
    try:
        amount = float(withdraw_amount_entry.get())
        result_label.config(text=atm.withdraw(amount))
    except ValueError:
        result_label.config(text="Please enter a valid amount.")

# Functions for Change PIN
def handle_change_pin():
    try:
        old_pin = old_pin_entry.get()
        new_pin = new_pin_entry.get()
        result_label.config(text=atm.change_pin(old_pin, new_pin))
    except:
        result_label.config(text="An error occurred. Please try again.")

# Main window
root = Tk()
root.title("ATM Simulator")
root.configure(background="#2E8B57")  # Setting background color to sea green

# Main Page (Front Page)
main_frame = Frame(root, bg="#2E8B57")
main_frame.pack(pady=50)

check_balance_button = Button(main_frame, text="Check Balance", font=("Helvetica", 14), bg="#4682B4", fg="white", command=goto_check_balance)
check_balance_button.pack(padx=10, pady=5)

deposit_button = Button(main_frame, text="Deposit", font=("Helvetica", 14), bg="#4682B4", fg="white", command=goto_deposit)
deposit_button.pack(padx=10, pady=5)

withdraw_button = Button(main_frame, text="Withdraw", font=("Helvetica", 14), bg="#4682B4", fg="white", command=goto_withdraw)
withdraw_button.pack(padx=10, pady=5)

change_pin_button = Button(main_frame, text="Change PIN", font=("Helvetica", 14), bg="#4682B4", fg="white", command=goto_change_pin)
change_pin_button.pack(padx=10, pady=5)

# Check Balance Frame
check_balance_frame = Frame(root, bg="#2E8B57")
check_balance_label = Label(check_balance_frame, text="Your Balance:", font=("Helvetica", 16), bg="#2E8B57", fg="white")
check_balance_label.pack(padx=10, pady=10)
result_label = Label(check_balance_frame, text="", font=("Helvetica", 16), bg="#2E8B57", fg="white")
result_label.pack(padx=10, pady=10)
check_balance_back_button = Button(check_balance_frame, text="Back", font=("Helvetica", 14), bg="#4682B4", fg="white", command=clear_screen)
check_balance_back_button.pack(padx=10, pady=10)

# Deposit Frame
deposit_frame = Frame(root, bg="#2E8B57")
deposit_amount_label = Label(deposit_frame, text="Enter Amount to Deposit:", font=("Helvetica", 16), bg="#2E8B57", fg="white")
deposit_amount_label.pack(padx=10, pady=10)
deposit_amount_entry = Entry(deposit_frame, font=("Helvetica", 16))
deposit_amount_entry.pack(padx=10, pady=10)
deposit_button = Button(deposit_frame, text="Deposit", font=("Helvetica", 14), bg="#4682B4", fg="white", command=handle_deposit)
deposit_button.pack(padx=10, pady=10)
deposit_back_button = Button(deposit_frame, text="Back", font=("Helvetica", 14), bg="#4682B4", fg="white", command=clear_screen)
deposit_back_button.pack(padx=10, pady=10)

# Withdraw Frame
withdraw_frame = Frame(root, bg="#2E8B57")
withdraw_amount_label = Label(withdraw_frame, text="Enter Amount to Withdraw:", font=("Helvetica", 16), bg="#2E8B57", fg="white")
withdraw_amount_label.pack(padx=10, pady=10)
withdraw_amount_entry = Entry(withdraw_frame, font=("Helvetica", 16))
withdraw_amount_entry.pack(padx=10, pady=10)
withdraw_button = Button(withdraw_frame, text="Withdraw", font=("Helvetica", 14), bg="#4682B4", fg="white", command=handle_withdraw)
withdraw_button.pack(padx=10, pady=10)
withdraw_back_button = Button(withdraw_frame, text="Back", font=("Helvetica", 14), bg="#4682B4", fg="white", command=clear_screen)
withdraw_back_button.pack(padx=10, pady=10)

# Change PIN Frame
change_pin_frame = Frame(root, bg="#2E8B57")
old_pin_label = Label(change_pin_frame, text="Old PIN:", font=("Helvetica", 14), bg="#2E8B57", fg="white")
old_pin_label.pack(padx=5, pady=5)
old_pin_entry = Entry(change_pin_frame, font=("Helvetica", 14), show="*")
old_pin_entry.pack(padx=5, pady=5)
new_pin_label = Label(change_pin_frame, text="New PIN:", font=("Helvetica", 14), bg="#2E8B57", fg="white")
new_pin_label.pack(padx=5, pady=5)
new_pin_entry = Entry(change_pin_frame, font=("Helvetica", 14), show="*")
new_pin_entry.pack(padx=5, pady=5)
change_pin_button = Button(change_pin_frame, text="Change PIN", font=("Helvetica", 14), bg="#4682B4", fg="white", command=handle_change_pin)
change_pin_button.pack(padx=5, pady=10)
change_pin_back_button = Button(change_pin_frame, text="Back", font=("Helvetica", 14), bg="#4682B4", fg="white", command=clear_screen)
change_pin_back_button.pack(padx=10, pady=10)

root.mainloop()
