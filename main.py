"""
My Python application idea is a personal finance manager.

The application will have the following features:

    - Users can create an account to track their expenses and income.
    - Users can add categories for their expenses and income, such as "rent," "groceries," "salary,"
     "freelance income," etc.
    - Users can add transactions, including the date, category, amount, and a short description.
    - Users can view summary statistics, such as total income, total expenses, net income,
     and average spending per category.
    - Users can export their data to a CSV file.

To implement this application, the following components will be used:

    1.) Validation of input received by the application:
    	- Validate user input, such as email and password during registration and login.
    	- Validate transaction data, such as the date, amount, and category ensuring they are the correct format and range.

    2.) Exception handling to deal with runtime errors:
    	- Handle runtime errors, such as database connection errors, file I/O errors, and user input errors.
    	- Use try-except blocks to handle exceptions gracefully.

    4.) Code organized with the help of classes or modules:
    	- Use classes to encapsulate data and behavior.
    	- Use modules to separate concerns and improve code readability and maintainability.

    5.) Data stored in files/databases:
    	- Use a CSV file to export user data.

    6.) Proper code documentation:
    	- Use descriptive variable names to make code more readable.
    	- Use docstrings for functions/methods to document their purpose and input/output parameters.
    	- Use type hinting to make code more maintainable and easier to understand.
    	- Use descriptive commit messages to track changes and document the development process.

Overall, this personal finance manager is a complex Python application that incorporates various elements of software
development, including validation, exception handling, code organization, data storage, and documentation.
"""
from account import *
import os


def create_account():
    user_account = Account()
    account_choice = ''
    while account_choice != 'q':
        print('Welcome to your account!')
        print('Please choose an option:')
        account_choice = input('q - quit\nn - new transaction\nr - remove a transaction\ne - export account info to '
                               'csv file\nv - view all transactions\nb - view current balance')
        if account_choice == 'n':
            category = input(f'Enter a category for transaction number:{user_account.get_transaction_number()}\n')
            date = input('Enter a date for the transaction:\n')
            amount = float(input('Enter an amount for the transaction:\n'))
            description = input('Enter a short description for the transaction:\n')
            user_account.add_transaction(category, date, amount, description)
        elif account_choice == 'r':
            transaction_to_remove = input('Choose a transaction number to remove:\n')
            user_account.remove_transaction(transaction_to_remove)
        elif account_choice == 'e':
            pass
        elif account_choice == 'v':
            print(user_account.get_transactions())
        elif account_choice == 'b':
            print(f'Current balance is: {user_account.get_balance()}')


def load_account_from_csv(file_path):
    pass


if __name__ == '__main__':
    print('Welcome to the personal finance manager!')
    user_choice = ''
    while user_choice != 'q':
        print('Please choose an option:')
        user_choice = input('q - quit\nn - new account\nr - read account info from csv file\n')
        if user_choice == 'n':
            create_account()
        elif user_choice == 'r':
            csv_path = input('Please input the path for the csv file.\n')
            load_account_from_csv(csv_path)
