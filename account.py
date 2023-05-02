class Account:
    __transaction_number: int
    __transactions: dict
    __balance: float

    def __init__(self):
        """
        Method to initialize an Account object.
        """
        self.__balance = 0
        self.__transactions = {}
        self.__transaction_number = 1

    def add_transaction(self, category: str = '', date: str = '', amount: float = 0, description: str = '') -> None:
        """
        Method to add a transaction to the Account object.
        :param category: Category for the transaction.
        :param date: Date for the transaction.
        :param amount: Dollar amount for the transaction.
        :param description: Description for the transaction.
        """
        self.__transactions[self.__transaction_number] = [category, date, amount, description]
        self.__transaction_number += 1
        self.__balance += amount

    def remove_transaction(self, transaction: int) -> None:
        """
        Method to remove a transaction from the Account object.
        :param transaction: Number of the transaction.
        """
        self.__balance -= self.__transactions[transaction][2]
        self.__transactions.pop(transaction)

    def get_balance(self) -> float:
        """
         Method to return the current balance of the Account object.
        :return: Returns the current balance as a float
        """
        return self.__balance

    def get_transactions(self) -> dict:
        """
        Method to return the transactions of the Account object.
        :return: Returns the dictionary of transactions.
        """
        return self.__transactions

    def get_transaction_number(self) -> int:
        """
        Method to return the current transaction number of the Account object.
        :return: Returns the current transaction number as an int
        """
        return self.__transaction_number
