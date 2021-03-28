#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    cur.execute("SELECT *FROM cities as city INNER JOIN states as state ON\
    city.state_id = state.id ORDER BY city.id")
    city_l = []
    for city in cur.fetchall():
        if city[4] == sys.argv[4]:
            city_l.append(city[2])
    print(", ".join(city_l))
