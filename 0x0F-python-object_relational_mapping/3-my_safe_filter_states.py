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
    cursor.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY id ASC".format(argv[4],))
    states = cursor.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    cursor.close()
    db.close()
