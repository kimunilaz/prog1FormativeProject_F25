# Personal Budget Tracker

## Project Overview
The Personal Budget Tracker is a Python command-line application for managing personal finances. Users can track income and expenses, categorize transactions, filter data, and view budget summaries. All data is stored in memory during the session, making it lightweight and simple to use.

## Features
- **Add Income/Expense**: Record transactions with date, amount, category, and description
- **List Transactions**: View all transactions in a formatted table
- **Filter**: Filter by type (income/expense), category, or month (YYYY-MM)
- **Summary**: View total income, expenses, balance, and per-category breakdowns
- **Input Validation**: Handles invalid dates, amounts, and menu choices gracefully

**Technical Implementation**: Uses OOP with Transaction base class, Income and Expense subclasses, and BudgetTracker class. Implements inheritance, collections (lists/dictionaries), and proper error handling.

## How to Run
1. Ensure Python 3.6+ is installed
2. Navigate to project folder: `cd path/to/folder`
3. Run: `python budget_tracker.py`
4. Follow the on-screen menu

## Menu Structure
```
1) Add income
2) Add expense
3) List transactions
4) Filter transactions
5) Show summary
0) Exit
```

## Sample Interactions

**Adding Income:**
```
Select an option: 1
Date (YYYY-MM-DD): 2025-01-15
Amount: $3000
Category: salary
Description: Monthly salary
✓ Income of $3000.0 added successfully!
```

**Adding Expense:**
```
Select an option: 2
Date (YYYY-MM-DD): 2025-01-16
Amount: $150
Category: food
Description: Grocery shopping
✓ Expense of $150.0 added successfully!
```

**Listing Transactions:**
```
ALL TRANSACTIONS
Date       | Type     |   Amount | Category   | Description
2025-01-15 | Income   | $ 3000.00 | salary     | Monthly salary
2025-01-16 | Expense  | $  150.00 | food       | Grocery shopping
2025-01-17 | Expense  | $ 1200.00 | rent       | Monthly rent
```

**Filtering by Category:**
```
Select an option: 4
Choose filter type: 2
Enter category: food

FILTERED TRANSACTIONS (category: food)
Date       | Type     |   Amount | Category   | Description
2025-01-16 | Expense  | $  150.00 | food       | Grocery shopping
```

**Budget Summary:**
```
BUDGET SUMMARY
Total Income:    $   3000.00
Total Expenses:  $   1350.00
Balance:         $   1650.00

PER-CATEGORY BREAKDOWN:
Income by Category:
  Salary            $   3000.00

Expenses by Category:
  Food              $    150.00
  Rent              $   1200.00
```

## Code Structure

**Classes:**
- `Transaction` (base): Stores date, amount, category, description, type
- `Income` (subclass): Inherits from Transaction, type='income'
- `Expense` (subclass): Inherits from Transaction, type='expense'
- `BudgetTracker`: Manages transactions with methods: add_income(), add_expense(), list_transactions(), filter_transactions(), show_summary()

**Functions:**
- `validate_amount()`: Ensures positive numeric input
- `validate_date()`: Validates YYYY-MM-DD format
- `main()`: Main program loop with menu



---
**Author**: [Your Name] | **Date**: December 2025 | **Course**: [Course Name]
