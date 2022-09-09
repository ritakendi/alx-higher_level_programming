#!/usr/bin/python3
import sys
import MySQLdb
import pycodestyle

"""a script that lists all states
    from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost",
                                    user=sys.argv[1],
                                    passwd=sys.argv[2],
                                    db=sys.argv[3],
                                    port=3306)
    cur = db_connection.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    result = cur.fetchall()
    for row in result:
        print(row)