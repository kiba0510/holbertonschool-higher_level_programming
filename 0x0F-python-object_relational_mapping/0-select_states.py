#!/usr/bin/python3
import MySQLdb
import sys
"""Script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    '''Connect to MySQL server'''
    
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    
    '''Instatiate a MySQL Curso Object'''
    cursor = db.cursor()
    
    '''Execute the DataBase operation'''
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    '''Fetch the row of a query and return a list of tuple'''
    for row in cursor.fetchall():
        print(row)

    '''Close cursor, resets results and ensures that the cursor object
    has no reference to its original connection object'''
    cursor.close()
    db.close()
