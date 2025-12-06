

from datetime import datetime


# Base Transaction class
class Transaction:
    def __init__(self, date, amount, category, description, type):
        self.date = date
        self.amount = float(amount)
        self.category = category.lower().strip()
        self.description = description
        self.type = type  # 'income' or 'expense'

#a method to enable printing an object
    def __str__(self):
        return f"{self.date} | {self.type.capitalize():8} | ${self.amount:>..2f} | {self.category:15} | {self.description}"

#Extract YYYY-MM format from date
    def get_month(self):

        return self.date[:7]




# Income subclass
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'income') # inheriting attributes from transaction class(parent class)


# Expense subclass
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'expense')# inheriting attributes from transaction class(parent class)


# BudgetTracker class to manage all transactions
class BudgetTracker:
    def __init__(self):
        self.transactions = [] #creates an empty list where transactions are to be stored

    def add_income(self, date, amount, category, description):
        myincome = Income(date, amount, category, description) # add an income transaction
        self.transactions.append(myincome)
        print(f"✓ Income of ${amount} added successfully!")

    def add_expense(self, date, amount, category, description):
        expense = Expense(date, amount, category, description) #add an expense transaction
        self.transactions.append(expense)
        print(f"✓ Expense of ${amount} added successfully!")

def menu():
    Tracker = BudgetTracker() # create an object to store transactions

    while True:
        print("\n")
        print (" BUDGET TRACKER MENU")
        print("\n")
        print("1) Add income")
        print("2) Add expense")
        #print("3) List transactions")
        #print("4) Filter transactions")
        #print("5) Show summary")
        #print("0) Exit")
        print("\n")

        choice = input("Select an option: ").strip()
        if choice == "1":
            date = (input("Enter a date: "))
            amount = input("Enter a amount: ").strip()
            category = input("Enter a category: ").strip()
            description = input("Enter a description: ").strip()

            Tracker.add_income(date, amount, category, description)


        if choice == "2":
            date = input("Enter a date: ").strip()
            amount = input("Enter a amount: ").strip()
            category = input("Enter a category: ").strip()
            description = input("Enter a description: ").strip()

            Tracker.add_expense(date, amount, category, description)



        break
 # TESTING
print(menu())