import calendar
import datetime
from expense import Expense


def main():
    print('Running Expense Tracker')
    expense_file_path = 'expenses.csv'
    budget = 2000

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print('Get User Expense')
    expense_name = input('Enter expense name: ')
    expense_amount = float(input('Enter expense amount: '))
    print(f"You've entered {expense_name}.")
    print(f"You've entered {expense_amount}.")

    expense_categories = [
        "🍔 Food",
        "🏠 Rent",
        "💼 Work",
        "🎉 Fun",
        "❓ Misc",
    ]

    while True:
        print('Select a category: ')
        for i, category_name in enumerate(expense_categories):
            print(f'{i + 1}. {category_name}')

        value_range = (f'[1 - {len(expense_categories)}]')
        selected_index = int(input(f'Enter a category number {value_range}: ')) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, 
                category= selected_category, 
                amount= expense_amount
            )
            return new_expense
        else:
            print('Invaild category. Please try again!')


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f'Save User Expense: {expense} to {expense_file_path}')
    with open(expense_file_path, 'a') as f:
        f.write(f'{expense.name},{expense.amount},{expense.category}\n')

def summarize_expenses(expense_file_path, budget):
    print('Summarize Expense')
    print('-------------------------------------------------')
    expenses: list[Expense] = []
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print('Expenses By Category 📈:')
    for key, amount in amount_by_category.items():
        print(f' {key}: ${amount:.2f}')

    print('-------------------------------------------------')

    total_spent = sum([x.amount for x in expenses])
    print('💵 Total Spent:' + red(f' ${total_spent:.2f}'))

    remaining_budget = budget - total_spent
    print(f"💰 Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print('👉 Budget Per Day:' + green(f' ${daily_budget:.2f}'))

def green(text):
    return f"\033[92m{text}\033[0m"

def red(text):
    return f"\033[31m{text}\033[0m"


if __name__ == '__main__':
    main()