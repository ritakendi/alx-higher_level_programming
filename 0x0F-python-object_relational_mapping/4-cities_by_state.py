#!/usr/bin/python3
"""
    lists all cities from the database hbtn_0e_4_usa
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
    c.execute("""SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states_id ORDER BY id ASC""")
    # returns a list of states inthe database.
    result = c.fetchall()

    # print states one by one
    for row in result:
        print(row)
    c.close()
