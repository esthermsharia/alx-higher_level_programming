#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host="localhost",
        port=3306,
        db=sys.argv[3],
        )
    cur = db.cursor()
    cur.execute("SELECT city.id, city.name, state.name FROM cities as city\
    INNER JOIN states as state ON city.state_id = state.id ORDER BY city.id")
    for city in cur.fetchall():
        print(city)
