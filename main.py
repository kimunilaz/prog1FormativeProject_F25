

from datetime import datetime


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

    #Display budget summary with totals
    def show_summary(self):

        # Check if there are any transactions
        if not self.transactions:
            print("\nNo transactions to summarize.")
            return

        # Calculate total income
        total_income = 0
        for transaction in self.transactions:
            if transaction.type == 'income':
                total_income = total_income + transaction.amount

        # Calculate total expenses
        total_expenses = 0
        for transaction in self.transactions:
            if transaction.type == 'expense':
                total_expenses = total_expenses + transaction.amount

        # Calculate balance (income - expenses)
        balance = total_income - total_expenses

        # Calculate per-category totals
        category_totals = {}
        for transaction in self.transactions:
            # Create a key like "income:salary" or "expense:food"
            key = transaction.type + ":" + transaction.category

            # If this category exists, add to it. If not, start at 0
            if key in category_totals:
                category_totals[key] = category_totals[key] + transaction.amount
            else:
                category_totals[key] = transaction.amount

        # Display the main summary
        print("\n")
        print("BUDGET SUMMARY")
        print("\n")
        print(f"Total Income:    ${total_income:>10.2f}")
        print(f"Total Expenses:  ${total_expenses:>10.2f}")
        print("\n")
        print(f"Balance:         ${balance:>10.2f}")


        print("\nPER-CATEGORY BREAKDOWN:")
        print("\n")

        # Separate income and expense categories
        income_categories = {}
        expense_categories = {}

        for key, amount in category_totals.items():
            # Split "income:salary" into type and category
            parts = key.split(':')
            transaction_type = parts[0]
            category_name = parts[1]

            if transaction_type == 'income':
                income_categories[category_name] = amount
            else:
                expense_categories[category_name] = amount

        # Display income by category
        if len(income_categories) > 0:
            print("\nIncome by Category:")
            for category, amount in sorted(income_categories.items()):
                print(f"  {category.capitalize():20} ${amount:>10.2f}")

        # Display expenses by category
        if len(expense_categories) > 0:
            print("\nExpenses by Category:")
            for category, amount in sorted(expense_categories.items()):
                print(f"  {category.capitalize():20} ${amount:>10.2f}")


def validate_amount(prompt):
    #Validate numeric input for amount
    while True:
        try:
            amount = input(prompt)
            amount_float = float(amount)
            if amount_float <= 0:
                print("Amount must be positive. Try again.")
                continue
            return amount_float
        except ValueError:
            print("Invalid amount. Please enter a number.")


def validate_date(prompt):
    #Validate date format YYYY-MM-DD
    while True:
        date = input(prompt)
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD (e.g., 2025-01-15)")



def main():
    tracker = BudgetTracker() # create an object to store transactions

    while True:
        print("\n")
        print (" BUDGET TRACKER MENU")
        print("\n")
        print("1) Add income")
        print("2) Add expense")
        print("3) List transactions")

        print("4) Filter transactions")
        print("5) Show summary")
        print("0) Exit")

        print("\n")



        choice = input("Select an option: ").strip()
        if choice == "1":
            date = (input("Enter a date YYYY-MM-DD: "))
            amount = input("Enter a amount: ").strip()
            category = input("Enter a category: ").strip()
            description = input("Enter a description: ").strip()

            tracker.add_income(date, amount, category, description)


        elif choice == "2":
            date = input("Enter a date 'YYYY-MM-DD': ").strip()
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

        elif choice == '5':
            tracker.show_summary()

        elif choice == '0':
            print("\n")
            print("Thank you for using Budget Tracker! Goodbye! 👋")
            print("\n")
            break




if __name__ == "__main__":
    main()