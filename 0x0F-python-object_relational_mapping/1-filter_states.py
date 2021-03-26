#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
    Script that lists all states with a name
    starting with N (upper N) from the database hbtn_0e_0_usa
    '''
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
