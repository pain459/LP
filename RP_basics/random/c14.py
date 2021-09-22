# Working with databases.
import sqlite3

with sqlite3.connect(":memory:") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    time = cursor.execute(query).fetchone()[0]

print(time)

# Working with database tables.

import sqlite3
import os
connection = sqlite3.connect(os.path.join(os.getcwd(), "test.db"))
cursor = connection.cursor()
cursor.execute(
    """CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );"""
)
cursor.execute(
    """INSERT INTO People VALUES(
            'Ron',
            'Obvious',
            42
        );"""
)
# connection.commit()
# connection.close()

# Execute multiple SQL statements
import sqlite3
import os

with sqlite3.connect(os.path.join(os.getcwd(), "test1.db")) as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS People;
            CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
            );
            INSERT INTO People VALUES(
                'Ron',
                'Obvious',
                '42'
            );"""
    )
