from datetime import datetime


# Base Transaction class
class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        self.date = date
        self.amount = float(amount)
        self.category = category.lower().strip()
        self.description = description
        self.type = ttype  # 'income' or 'expense'

    def __str__(self):
        return f"{self.date} | {self.type.capitalize():8} | ${self.amount:>8.2f} | {self.category:15} | {self.description}"

    def get_month(self):
        """Extract YYYY-MM format from date"""
        return self.date[:7]


# Income subclass
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'income')


# Expense subclass
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'expense')


# BudgetTracker class to manage all transactions
class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, date, amount, category, description):
        """Add an income transaction"""
        income = Income(date, amount, category, description)
        self.transactions.append(income)
        print(f"✓ Income of ${amount} added successfully!")

    def add_expense(self, date, amount, category, description):
        """Add an expense transaction"""
        expense = Expense(date, amount, category, description)
        self.transactions.append(expense)
        print(f"✓ Expense of ${amount} added successfully!")

    def list_transactions(self):
        """Display all transactions"""
        if not self.transactions:
            print("\nNo transactions recorded yet.")
            return

        print("\n" + "=" * 90)
        print("ALL TRANSACTIONS")
        print("=" * 90)
        print(f"{'Date':10} | {'Type':8} | {'Amount':>8} | {'Category':15} | Description")
        print("-" * 90)

        for t in self.transactions:
            print(t)
        print("=" * 90)

    def filter_transactions(self, filter_type=None, filter_value=None):
        """Filter transactions by type, category, or month"""
        if not self.transactions:
            print("\nNo transactions to filter.")
            return

        filtered = self.transactions

        if filter_type == 'type' and filter_value:
            filtered = [t for t in filtered if t.type == filter_value.lower()]
        elif filter_type == 'category' and filter_value:
            filtered = [t for t in filtered if t.category == filter_value.lower().strip()]
        elif filter_type == 'month' and filter_value:
            filtered = [t for t in filtered if t.get_month() == filter_value]

        if not filtered:
            print(f"\nNo transactions found matching the filter.")
            return

        print("\n" + "=" * 90)
        print(f"FILTERED TRANSACTIONS ({filter_type}: {filter_value})")
        print("=" * 90)
        print(f"{'Date':10} | {'Type':8} | {'Amount':>8} | {'Category':15} | Description")
        print("-" * 90)

        for t in filtered:
            print(t)
        print("=" * 90)

    def show_summary(self):
        """Display budget summary with totals"""
        if not self.transactions:
            print("\nNo transactions to summarize.")
            return

        total_income = sum(t.amount for t in self.transactions if t.type == 'income')
        total_expenses = sum(t.amount for t in self.transactions if t.type == 'expense')
        balance = total_income - total_expenses

        # Per-category totals
        category_totals = {}
        for t in self.transactions:
            key = f"{t.type}:{t.category}"
            category_totals[key] = category_totals.get(key, 0) + t.amount

        print("\n" + "=" * 60)
        print("BUDGET SUMMARY")
        print("=" * 60)
        print(f"Total Income:    ${total_income:>10.2f}")
        print(f"Total Expenses:  ${total_expenses:>10.2f}")
        print("-" * 60)
        print(f"Balance:         ${balance:>10.2f}")
        print("=" * 60)

        print("\nPER-CATEGORY BREAKDOWN:")
        print("-" * 60)

        # Group by type
        income_cats = {k.split(':')[1]: v for k, v in category_totals.items() if k.startswith('income')}
        expense_cats = {k.split(':')[1]: v for k, v in category_totals.items() if k.startswith('expense')}

        if income_cats:
            print("\nIncome by Category:")
            for cat, amt in sorted(income_cats.items()):
                print(f"  {cat.capitalize():20} ${amt:>10.2f}")

        if expense_cats:
            print("\nExpenses by Category:")
            for cat, amt in sorted(expense_cats.items()):
                print(f"  {cat.capitalize():20} ${amt:>10.2f}")

        print("=" * 60)


def validate_amount(prompt):
    """Validate numeric input for amount"""
    while True:
        try:
            amount = input(prompt)
            amount_float = float(amount)
            if amount_float <= 0:
                print("❌ Amount must be positive. Try again.")
                continue
            return amount_float
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")


def validate_date(prompt):
    """Validate date format YYYY-MM-DD"""
    while True:
        date = input(prompt)
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD (e.g., 2025-01-15)")


def main():
    tracker = BudgetTracker()

    print("\n" + "=" * 60)
    print("          PERSONAL BUDGET TRACKER")
    print("=" * 60)

    while True:
        print("\n" + "-" * 60)
        print("MENU:")
        print("-" * 60)
        print("1) Add income")
        print("2) Add expense")
        print("3) List transactions")
        print("4) Filter transactions")
        print("5) Show summary")
        print("0) Exit")
        print("-" * 60)

        choice = input("Select an option: ").strip()

        if choice == '1':
            print("\n--- ADD INCOME ---")
            date = validate_date("Date (YYYY-MM-DD): ")
            amount = validate_amount("Amount: $")
            category = input("Category (e.g., salary, freelance): ").strip()
            description = input("Description: ").strip()
            tracker.add_income(date, amount, category, description)

        elif choice == '2':
            print("\n--- ADD EXPENSE ---")
            date = validate_date("Date (YYYY-MM-DD): ")
            amount = validate_amount("Amount: $")
            category = input("Category (e.g., food, rent, transport): ").strip()
            description = input("Description: ").strip()
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
                print("❌ Invalid filter option.")

        elif choice == '5':
            tracker.show_summary()

        elif choice == '0':
            print("\n" + "=" * 60)
            print("Thank you for using Budget Tracker! Goodbye! 👋")
            print("=" * 60)
            break

        else:
            print("❌ Invalid choice. Please select a valid option (0-5).")


if __name__ == "__main__":
    main()