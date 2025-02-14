'''
Carson Harbin
Programming Exercise 3
This program asks the user to provide an expense and then the price for that expense repeating until the user inputs "done"
and then provides the user with the total expense, highest expense, and lowest expense.
'''

from functools import reduce

def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of monthly expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: $"))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    return expenses

def analyze_expenses(expenses):
    if not expenses:
        print("No expenses entered.")
        return

    total_expense = reduce(lambda acc, x: acc + x[1], expenses, 0)
    highest_expense = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)
    lowest_expense = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    print("\nExpense Analysis:")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

def main():
    expenses = get_expenses()
    analyze_expenses(expenses)

if __name__ == "__main__":
    main()
