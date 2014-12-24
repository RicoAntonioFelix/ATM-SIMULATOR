# Copyright 2014 Rico Antonio Felix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class BankAccount:
    """Simplistic model of a bank account.

    This module provides a simple abstraction to the notion of a bank account.

    It provides storage for:
    -> account number
    -> first name
    -> last name
    -> account balance

    Along with the above storage mechanisms, it provides operations for accessing
    the stored information and manipulating it.

    Creation and usage of an instance of this component is as follows:
     myAccount = BankAccount(12345, 'John', 'Doe', 500)
     myAccount.deposit(500)
     myAccount.withdraw(300)
     bankStatement = myAccount.get_account_details()
     print(bankStatement)
     """

    def __init__(self, account_number, first_name, last_name, initial_balance):
        """Initializes a bank account object with the specified arguments.

        Checks that the arguments passed in are of the correct types else an 'Exception' is raised.

        :param account_number: Account number associated with the account
        :param first_name: First name associated with the account
        :param last_name: Last name associated with the account
        :param initial_balance: Initial balance associated with the account
        :return: An initialized object with the specified arguments
        """
        self.__validate_type_invariants__(account_number, first_name, last_name, initial_balance)
        self.__account_number__ = account_number
        self.__first_name__ = first_name
        self.__last_name__ = last_name
        self.__balance__ = initial_balance if initial_balance >= 0 else 0

    def get_account_number(self):
        """Get the object's stored account number."""
        return self.__account_number__

    def set_first_name(self, first_name):
        """Change the first name field of the object.

        Checks that the argument passed in is of type 'str' else an 'Exception' is raised.

        :param first_name: New name to overwrite the previously stored name
        :return: None
        """
        if type(first_name) != str:
            raise Exception("Invalid argument: first_name of type {} should be: <class 'str'>".format(type(first_name)))
        self.__first_name__ = first_name

    def get_first_name(self):
        """Get the object's stored first name.

        :return: Current first name associated with the account
        """
        return self.__first_name__

    def set_last_name(self, last_name):
        """Change the last name field of the object.

        Checks that the argument passed in is of type 'str' else an 'Exception' is raised.

        :param last_name: New name to overwrite the previously stored name
        :return: None
        """
        if type(last_name) != str:
            raise Exception("Invalid argument: last_name of type {} should be: <class 'str'>".format(type(last_name)))
        self.__last_name__ = last_name

    def get_last_name(self):
        """Get the object's stored last name.

        :return: Current last name associated with the account
        """
        return self.__last_name__

    def get_balance(self):
        """Get the object's stored balance.

        :return: Current account balance
        """
        return self.__balance__

    def deposit(self, amount):
        """Increments the current balance by the specified amount.

        Checks that the argument passed in is of type 'int' else an 'Exception' is raised.

        If the amount specified is less than zero(0), no operation is performed and the balance remains unchanged.

        :param amount: Amount to increment the current balance
        :return: None
        """
        if type(amount) != int:
            raise Exception("Invalid argument: amount of type {} should be: <class 'int'>".format(type(amount)))
        self.__balance__ += amount if amount > 0 else 0

    def withdraw(self, amount):
        """Decrements the current balance by the specified amount if its less than or equal to the current balance and
        returns the specified amount. If amount specified is greater than the current balance, no operation is
        performed, the balance remains unchanged and zero(0) is returned.

        Checks that the argument passed in is of type 'int' else an 'Exception' is raised.

        :param amount: Amount to decrement the current balance
        :return: Amount specified if its less than or equal to the current balance
        """
        if type(amount) != int:
            raise Exception("Invalid argument: amount of type {} should be: <class 'int'>".format(type(amount)))
        if amount <= self.__balance__:
            self.__balance__ -= amount
            return amount
        else:
            return 0

    def get_account_details(self):
        """Returns a string representation with the current state of the object which includes the
        current account number, first name, last name and balance in the following format:

        Account Number: [account_number]
        Name: [first_name & last_name]
        Balance: [balance]

        :return: String representation of the current state of the object
        """
        return "Account Number: {}\nName: {}\nBalance: ${}".format(self.__account_number__, (self.__first_name__ + ' ' +
                                                                                             self.__last_name__),
                                                                   self.__balance__)

    @classmethod
    def __validate_type_invariants__(cls, account_number, first_name, last_name, initial_balance):
        """\
        Simply checks that arguments passed in is of the appropriate type for initialization of an object of this type
        else an 'Exception' is raised.
        """
        if type(account_number) != str:
            raise Exception('Invalid argument: account_number of type {} should be: {}'.format(type(account_number),
                                                                                               "<class 'str'>"))
        if type(first_name) != str:
            raise Exception('Invalid argument: first_name of type {} should be: {}'.format(type(first_name),
                                                                                           "<class 'str'>"))

        if type(last_name) != str:
            raise Exception('Invalid argument: last_name of type {} should be: {}'.format(type(last_name),
                                                                                          "<class 'str'>"))

        if type(initial_balance) != int:
            raise Exception('Invalid argument: initial_balance of type {} should be: {}'.format(type(account_number),
                                                                                                "<class 'int'>"))
