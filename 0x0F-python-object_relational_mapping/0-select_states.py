#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to MySQL server
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Execute query to get all states
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Print results
    for row in cur.fetchall():
        print(row)

    # Close database connection
    cur.close()
    conn.close()

