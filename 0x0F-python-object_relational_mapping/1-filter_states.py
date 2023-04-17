#!/usr/bin/python3

"""
All names starting from letter 'N'
is list in this script from database 'hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Query should be executed to get states that begin with the letter 'N'
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

