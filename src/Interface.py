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

from ATM import ATM

# ----------------------------------------------------------
# Initialize the ATM
# ----------------------------------------------------------
atm = ATM()

account = None  # account for processing

# ----------------------------------------------------------
# Access point: get user pin
# ----------------------------------------------------------
pin = atm.get_input("Enter your pin and press [enter] to continue: ")

# ----------------------------------------------------------
# Validation: check pin
# Give user three(3) tries to get it correct
# ----------------------------------------------------------
tries = 0
while tries <= 2:
    if atm.validate_pin(pin):
        account = atm.load_account(pin)
        break
    else:
        if tries == 2:
            exit("Goodbye...")
        tries += 1
        print("That pin is invalid, you have {} more {}".format(3 - tries, "tries" if tries == 1 else "try"))
        pin = atm.get_input("Enter your pin and press [enter] to continue: ")

# ----------------------------------------------------------
# Initialize transactions loop
# ----------------------------------------------------------
while True:
    atm.menu()
    option = int(atm.get_input("Enter option: "))

    if option == 1:
        account.withdraw(int(atm.get_input("Enter amount to withdraw: ")))
    elif option == 2:
        account.deposit(int(atm.get_input("Enter amount to deposit: ")))
    elif option == 3:
        print(account.get_account_details())
    else:
        print("Invalid option\n")

    # ----------------------------------------------------------
    # Check for continuation
    # ----------------------------------------------------------
    if atm.get_input("Would you like to perform another transaction (Y/n): ").lower() == "y":
        continue
    else:
        break
