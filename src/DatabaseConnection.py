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

import sqlite3


class DatabaseConnection:
    """This class is used an as application specific model of a database connection.

    Can be used to perform all database CRUD actions which allows you to do the following:
    -> Create new records in the connected database
    -> Retrieve specified records from the connected database
    -> Update specified records in the connected database
    -> Delete specified records in the connected database

    To perform these operations correctly using this module, class constants are provided to determine how an operation
    should be performed.

    Class constants are:
    CREATE
    READ
    UPDATE
    DELETE

    Example of usage:
    connection = DatabaseConnection("expenses.db")
    connection.sql_statement(connection.CREATE, "CREATE TABLE expenses (month TEXT, year INT, expense FLOAT)")
    connection.sql_statement(connection.UPDATE, "INSERT INTO expenses (month, year, expense) VALUES ('Jan', 07, 200.99)")
    data_set = connection.sql_statement(connection.READ, "SELECT * FROM expenses")
    connection.sql_statement(connection.DELETE, "DELETE * FROM expenses")
    connection.sql_statement(connection.DELETE, "DROP TABLE IF EXIST expenses")
    """

    def __init__(self, database_file):
        """Initializes a database-connection object to interact with the specified local database.

        Checks that the argument passed in is of type 'str' else an 'Exception' is raised.

        :param database_file: The local database file to connect to
        :return: An initialized object with a connection to the specified database
        """
        if type(database_file) != str:
            raise Exception(
                "Invalid argument: database_file of type {} should be: <class 'str'>".format(type(database_file)))
        self.__database__ = sqlite3.connect(database_file)
        self.CREATE = 0
        self.READ = 1
        self.UPDATE = 2
        self.DELETE = 3

    def sql_statement(self, operation, sql):
        """Performs CRUD operations on the connected database.

        Checks that the argument 'operation' passed in is valid else an 'Exception' is raised.
        Checks that the argument 'sql' passed in is of type 'str' else an 'Exception' is raised.

        :param operation: Operation to perform on the connected database
        :param sql: SQL statement to transmit to the underlying database engine
        :return: If a READ operation is to be performed, the result set is returned
        """
        if type(sql) != str:
            raise Exception(
                "Invalid argument: sql of type {} should be: <class 'str'>".format(type(sql)))
        if operation == 0 or operation == 2 or operation == 3:
            self.__database__.execute(sql)
        elif operation == 1:
            return self.__database__.execute(sql)
        else:
            raise Exception("Invalid SQL operation code")

    def close(self):
        """Closes the connection to the database."""
        self.__database__.close()
