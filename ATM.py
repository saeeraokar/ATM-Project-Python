#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from datetime import datetime

class ATM:
    def __init__(self, balance=0, pin="1234", daily_limit=20000):
        self.balance = balance
        self.pin = pin
        self.history = []
        self.daily_limit = daily_limit
        self.daily_withdrawn = 0
        self.today = datetime.now().date()

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print("Login Successful!\n")
            return True
        else:
            print("Invalid PIN. Access Denied.")
            return False

    def reset_daily_limit(self):
        if datetime.now().date() != self.today:
            self.today = datetime.now().date()
            self.daily_withdrawn = 0

    def check_balance(self):
        print(f"\n Your Balance: ₹{self.balance}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print(" Enter a valid amount!\n")
                return
        except ValueError:
            print(" Invalid input!\n")
            return

        self.balance += amount
        self.history.append(f"Deposited ₹{amount} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" ₹{amount} Deposited Successfully!\n")
        self.print_receipt("Deposit", amount)

    def withdraw(self):
        self.reset_daily_limit()
        remaining_limit = self.daily_limit - self.daily_withdrawn
        print(f" Remaining Daily Withdrawal Limit: ₹{remaining_limit}")

        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print(" Enter a valid amount!\n")
                return
        except ValueError:
            print("Invalid input!\n")
            return

        if amount > self.balance:
            print("Insufficient Balance!\n")
        elif amount > remaining_limit:
            print(f"Daily withdrawal limit exceeded! (Remaining: ₹{remaining_limit})\n")
        else:
            self.balance -= amount
            self.daily_withdrawn += amount
            self.history.append(f"Withdrew ₹{amount} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"₹{amount} Withdrawn Successfully!\n")
            self.print_receipt("Withdraw", amount)

    def show_history(self, mini=False):
        print("\n Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:

            transactions_to_show = self.history[-5:] if mini else self.history
            for h in transactions_to_show:
                print("-", h)

    def print_receipt(self, txn_type, amount):
        print("\n Transaction Receipt")
        print("--------------------------")
        print(f"Date/Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Transaction: {txn_type}")
        print(f"Amount     : ₹{amount}")
        print(f"Balance    : ₹{self.balance}")
        print("--------------------------\n")

    def menu(self):
        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Mini Statement (Last 5)")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.show_history()
            elif choice == "5":
                self.show_history(mini=True)
            elif choice == "6":
                print("\nThank you for using ATM. Goodbye!\n")
                break
            else:
                print(" Invalid Choice! Try again.\n")



atm = ATM(balance=10000, daily_limit=20000)
if atm.check_pin():
    atm.menu()


# In[ ]:





# In[ ]:




