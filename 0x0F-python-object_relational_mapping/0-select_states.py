#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Results are sorted in ascending order by states id.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    conn = db.cursor()
    conn.execute("SELECT * FROM `states`")
    for state in conn.fetchall():
        print(state)
