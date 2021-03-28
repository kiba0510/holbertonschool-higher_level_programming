#!/usr/bin/python3
"""Lists all cities from the database."""


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
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities\
    JOIN states\
    ON state_id=states.id\
    ORDER BY cities.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
