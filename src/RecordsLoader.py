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

from DatabaseConnection import DatabaseConnection
from BankAccount import BankAccount


class RecordsLoader:
    """Loads bank account records from local database file"""

    @staticmethod
    def load_records(database_file):
        """\
        Opens the specified local database file with the bank account records and store the
        records in-memory for usage with the aid of the dictionary data structure.

        Checks that the argument 'database_file' passed in is of type 'str' else an 'Exception' is raised.

        If the specified database file doesn't exist an 'Exception' is raised.

        :param database_file: Name of the database file to load records from
        :return: Dictionary data structure with the bank account records
        """
        if type(database_file) != str:
            raise Exception(
                "Invalid argument: database_file of type {} should be: <class 'str'>".format(type(database_file)))
        database = DatabaseConnection(database_file)
        records = dict()
        result_set = database.sql_statement(database.READ, "SELECT * FROM accounts")
        for record in result_set:  # grab each record from the result-set
            records[record[4]] = BankAccount(record[0], record[1], record[2], record[3])
        database.close()
        return records
