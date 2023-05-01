class Account:
    def __init__(self):
        self.__balance = 0
        self.__transactions = {}
        self.__transaction_number = 1

    def add_transaction(self, category, date, amount, description):
        self.__transactions[self.__transaction_number] = [category, date, amount, description]
        self.__transaction_number += 1

    def remove_transaction(self, transaction):
        self.__transactions.pop(transaction)

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def get_transaction_number(self):
        return self.__transaction_number
