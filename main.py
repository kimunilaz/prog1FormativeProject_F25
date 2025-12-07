

#from datetime import datetime


# Base Transaction class
class Transaction:
    def __init__(self, date, amount, category, description, tyype):
        self.date = date
        self.amount = float(amount)
        self.category = category.lower().strip()
        self.description = description
        self.type = tyype  # 'income' or 'expense'

#a method to enable printing an object
    def __str__(self):
        return f"{self.date} | {self.type.capitalize():8} | ${self.amount:>8.2f} | {self.category:15} | {self.description}"

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

    def list_transactions(self): #display transactions

        if not self.transactions:
            print("\nNo transactions recorded yet.")
            return

        print("\n")
        print("ALL TRANSACTIONS")
        print("\n")
        print(f"{'Date':10} | {'Type':8} | {'Amount':>8} | {'Category':15} | Description")
        print("\n")

        for t in self.transactions:
            print(t)

    def filter_transactions(self, filter_type=None, filter_value=None):
        """Filter transactions by type, category, or month"""
        # Check if there are any transactions
        if not self.transactions:
            print("\nNo transactions to filter.")
            return

        # Create empty list to store filtered results
        filtered = []

        # Filter by type (income or expense)
        if filter_type == 'type':
            for transaction in self.transactions:
                if transaction.type == filter_value.lower():
                    filtered.append(transaction)

        # Filter by category
        elif filter_type == 'category':
            for transaction in self.transactions:
                if transaction.category == filter_value.lower().strip():
                    filtered.append(transaction)

        # Filter by month
        elif filter_type == 'month':
            for transaction in self.transactions:
                if transaction.get_month() == filter_value:
                    filtered.append(transaction)

        # Check if we found any matching transactions
        if len(filtered) == 0:
            print(f"\nNo transactions found matching the filter.")
            return

        # Display the filtered transactions
        print("\n")
        print(f"FILTERED TRANSACTIONS ({filter_type}: {filter_value})")
        print("\n")
        print(f"{'Date':10} | {'Type':8} | {'Amount':>8} | {'Category':15} | Description")


        for transaction in filtered:
            print(transaction)
        print("=" * 90)

def main():
    tracker = BudgetTracker() # create an object to store transactions

    while True:
        print("\n")
        print (" BUDGET TRACKER MENU")
        print("\n")
        print("1) Add income")
        print("2) Add expense")
        print("3) List transactions")

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

            tracker.add_income(date, amount, category, description)


        elif choice == "2":
            date = input("Enter a date: ").strip()
            amount = input("Enter a amount: ").strip()
            category = input("Enter a category: ").strip()
            description = input("Enter a description: ").strip()

            tracker.add_expense(date, amount, category, description)

        elif choice == '3':
            tracker.list_transactions()

        elif choice == '4':
            print("\n--- FILTER TRANSACTIONS ---")
            print("Filter by:")
            print("  1) Type (income/expense)")
            print("  2) Category")
            print("  3) Month (YYYY-MM)")

            filter_choice = input("Choose filter type: ").strip()

            if filter_choice == '1':
                filter_val = input("Enter type (income/expense): ").strip()
                tracker.filter_transactions('type', filter_val)
            elif filter_choice == '2':
                filter_val = input("Enter category: ").strip()
                tracker.filter_transactions('category', filter_val)
            elif filter_choice == '3':
                filter_val = input("Enter month (YYYY-MM, e.g., 2025-10): ").strip()
                tracker.filter_transactions('month', filter_val)
            else:
                print(" Invalid filter option.")





 # TESTING
if __name__ == "__main__":
    main()