#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connect to a MySQL server."""

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY id ASC".format(argv[4]))
    states = cursor.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    cursor.close()
    db.close()
