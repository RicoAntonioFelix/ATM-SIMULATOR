# Copyright 2014 Rico Antonio Felix
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sqlite3


class DatabaseScript:
    """This module is used to populate the specified database with sample records for the purpose of simulation."""
    @staticmethod
    def load_database(database_file):
        """Populates the specified database file with sample data for simulation.

        If the specified database file already exist no operation is performed, else the file is created and populated
        with the sample data.

        Checks that the argument 'database_file' passed in is of type 'str' else an 'Exception' is raised.

        :param database_file: Name of the database file to populate with sample data
        :return: None
        """
        if type(database_file) != str:
            raise Exception(
                "Invalid argument: database_file of type {} should be: <class 'str'>".format(type(database_file)))
        if os.path.exists(database_file):
            return
        else:
            connection = sqlite3.connect(database_file)
            connection.execute(
                "CREATE TABLE accounts (account_number TEXT, first_name TEXT, last_name TEXT, balance INT, pin TEXT)")
            connection.execute(
                "INSERT INTO accounts (account_number, first_name, last_name, balance, pin)"
                " VALUES ('10001', 'David', 'Chen', 10000, '2050')")
            connection.execute(
                "INSERT INTO accounts (account_number, first_name, last_name, balance, pin)"
                " VALUES ('10002', 'Rico', 'Felix', 10000, '9014')")
            connection.execute(
                "INSERT INTO accounts (account_number, first_name, last_name, balance, pin)"
                " VALUES ('10003', 'Mark', 'Hurd', 120000, '5572')")
            connection.execute(
                "INSERT INTO accounts (account_number, first_name, last_name, balance, pin)"
                " VALUES ('10004', 'Susan', 'Barbara', 9000, '9393')")
            connection.execute(
                "INSERT INTO accounts (account_number, first_name, last_name, balance, pin)"
                " VALUES ('10005', 'Wayne', 'Mark', 250, '8226')")
            connection.execute(
                "INSERT INTO accounts (account_number, first_name, last_name, balance, pin)"
                " VALUES ('10006', 'Yevette', 'Pauline', 20, '1022')")
            connection.execute(
                "INSERT INTO accounts (account_number, first_name, last_name, balance, pin)"
                " VALUES ('10007', 'Maxwell', 'Richards', 300, '9584')")
            connection.commit()
            connection.close()
