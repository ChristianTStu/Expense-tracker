def main():
    print('Running Expense Tracker')

    # Get user input for expense.
    get_user_expense()

    # Write their expense to a file.
    save_expense_to_file()

    # Read file and summarize expenses.
    summarize_expense()


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
        selected_index = input(f'Enter a category number {value_range}: ')
        break

def save_expense_to_file():
    print('Save Expense to File')

def summarize_expense():
    print('Summarize Expense')


if __name__ == '__main__':
    main()