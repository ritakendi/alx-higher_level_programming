#!/usr/bin/python3
"""takes in an argumenyt(user input)
    and displays all values inthe states table
    where name matches the user input.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # arguments.
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # creating an instance of the 'cursor class' used to execute
    # 'SQL queries.
    c = db.cursor()

    """taking the cursor object and calling the execute function
        with the query and a tuple containing the values to substitute
    """
    c.execute("""SELECT * FROM cities  ORDER BY id ASC""")
    # returns a list of states inthe database.
    result = c.fetchall()

    # print states one by one
    for row in result:
        print(row)
    c.close()
