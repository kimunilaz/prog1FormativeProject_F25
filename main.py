

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




# Income subclass
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'income') # inheriting attributes from transaction class(parent class)


# Expense subclass
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'expense')# inheriting attributes from transaction class(parent class)

