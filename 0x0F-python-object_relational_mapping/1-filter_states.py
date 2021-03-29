#!/usr/bin/python3
"""
Lists all scripts with a name starting with "N".
Usage mysql <username> <passwd> <db name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id")
    for state in cur.fetchall():
        if state[1][0] == "N":
            print(state)
