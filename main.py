import os
from account import Account
import csv


def create_account(user_account: Account = Account()) -> None:
    """
    A function to create a user account and allow user to select choices to interact with their account.
    """
    print('Welcome to your account!')
    account_choice: str = ''
    while account_choice != 'q':
        print('Please choose an option:')
        account_choice = input('q - quit\nn - new transaction\nr - remove a transaction\ne - export account info to '
                               'csv file\nv - view all transactions\nb - view current balance\n')
        if account_choice == 'n':
            try:
                category: str = input(f'Enter a category for transaction number '
                                      f'{user_account.get_transaction_number()}\n')
                date: str = input('Enter a date for the transaction:\n')
                amount: float = float(input('Enter an amount for the transaction:\n'))
                description: str = input('Enter a short description for the transaction:\n')
                user_account.add_transaction(category, date, amount, description)
                print(f'The following transaction was added:\n'
                      f'Category: {user_account.get_transactions()[user_account.get_transaction_number() - 1][0]}\n'
                      f'Date: {user_account.get_transactions()[user_account.get_transaction_number() - 1][1]}\n'
                      f'Amount: {user_account.get_transactions()[user_account.get_transaction_number() - 1][2]:.2f}\n'
                      f'Description: {user_account.get_transactions()[user_account.get_transaction_number() - 1][3]}\n')
            except ValueError:
                print('Must enter a number for transaction amount!\n')
        elif account_choice == 'r':
            try:
                transaction_to_remove: int = int(input('Choose a transaction number to remove:\n'))
                user_account.remove_transaction(transaction_to_remove)
            except ValueError:
                print('Must enter a number!\n')
            except KeyError:
                print('Invalid transaction number!\n')
        elif account_choice == 'e':
            output_file = input('Enter a name for the output file:\n').strip()
            while os.path.isfile('files/' + output_file):
                response = input('Overwrite existing file (y/n): ').strip().lower()

                while response != 'y' and response != 'n':
                    response = input('Enter (y/n): ').strip().lower()

                if response == 'y':
                    break
                elif response == 'n':
                    filename = input('New output file name: ').strip()
            with open(('files/' + output_file), 'w', newline='') as csv_output:
                csv_content = csv.writer(csv_output)
                csv_content.writerow(['Category', 'Date', 'Amount', 'Description'])
                account_transactions = user_account.get_transactions()
                for transaction in account_transactions:
                    csv_content.writerow([account_transactions[transaction][0], account_transactions[transaction][1],
                                          account_transactions[transaction][2], account_transactions[transaction][3]])
            print('Account saved!\n')
        elif account_choice == 'v':
            account_transactions = user_account.get_transactions()
            for transaction in account_transactions:
                print(f'Transaction {transaction}:\n'
                      f'Category: {account_transactions[transaction][0]}\n'
                      f'Date: {account_transactions[transaction][1]}\n'
                      f'Amount: {account_transactions[transaction][2]:.2f}\n'
                      f'Description: {account_transactions[transaction][3]}\n')
        elif account_choice == 'b':
            print(f'Current balance is: ${user_account.get_balance():.2f}\n')
        elif account_choice == 'q':
            pass
        else:
            print('Must enter a valid option!\n')


def load_account_from_csv(file_path: str) -> None:
    """
    A function to allow loading of an account from a csv file.
    :param file_path: Variable containing the path of the csv file.
    """
    user_account = Account()
    with open(file_path, 'r') as input_file:
        csv_reader = csv.reader(input_file)
        for line in csv_reader:
            try:
                float(line[2])
            except ValueError:
                continue
            else:
                category = line[0]
                date = line[1]
                amount = float(line[2])
                description = line[3]
                user_account.add_transaction(category, date, amount, description)
        print('Account loaded successfully!')
        create_account(user_account)


if __name__ == '__main__':
    print('Welcome to the personal finance manager!')
    user_choice: str = ''
    while user_choice != 'q':
        print('Please choose an option:')
        user_choice = input('q - quit\nn - new account\nr - read account info from csv file\n')
        if user_choice == 'n':
            create_account()
        elif user_choice == 'r':
            csv_name: str = input('Please input the name of the csv file.\n').strip()
            if os.path.isfile('files/' + csv_name):
                file_path = 'files/' + csv_name
                load_account_from_csv(file_path)
            else:
                print('File not found!\n')
        elif user_choice == 'q':
            pass
        else:
            print('Must enter a valid option!\n')
