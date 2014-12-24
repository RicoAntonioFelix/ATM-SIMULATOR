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

from DatabaseScript import DatabaseScript
from RecordsLoader import RecordsLoader


class ATM:
    """Primitive model of an ATM machine

    * Performs pin validation
    * Contains a menu and simulated keypad for user interaction
    """

    def __init__(self):
        """Initializes the object by loading its memory with the bank account records from the database.

        :return: ATM object with its memory initialized with the database records
        """
        DatabaseScript.load_database("accounts.db")
        self.__memory__ = RecordsLoader.load_records("accounts.db")

    def validate_pin(self, pin):
        """Checks if the pin is valid

        Checks that the argument passed in is of type 'str' else an error message is displayed and no operation is
        performed.

        :param pin: Pin to perform validation
        :return: True if the pin is valid else returns False
        """
        if self.param_is_good(pin):
            return pin in self.__memory__

    @staticmethod
    def menu():
        """Provides a menu for the interface."""
        print("Press 1 for withdraw")
        print("Press 2 for deposit")
        print("Press 3 for account balance")

    def get_input(self, message):
        """Get input from the user.

        Checks that the argument passed in is of type 'str' else an error message is displayed and no operation is
        performed.

        :param message: Prompt message for the user to follow
        :return: User input as a 'str'
        """
        if self.param_is_good(message):
            return input(message)

    def load_account(self, pin):
        """Get bank account record associated with the pin.

        Checks that the argument passed in is of type 'str' else an error message is displayed and no operation is
        performed.

        :param pin: Pin to locate the associated bank account record
        :return: Bank account record associated with the pin
        """
        if self.param_is_good(pin):
            return self.__memory__.get(pin)

    @classmethod
    def param_is_good(cls, param):
        """Performs argument type validation.

        :param param: Argument for checking type information
        :return: True if argument is of the appropriate type else returns False
        """
        if type(param) != str:
            print("Argument should be of type <class 'str'> found {}".format(type(param)))
            return False
        return True
