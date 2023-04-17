#!/usr/bin/python3

"""
All names starting from letter 'N'
is list in this script from database 'hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

# Access the database and get states
db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                     passwd=sys.argv[2], db=sys.argv[3])

# Execute query to get states whose name starts with 'N'
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

# Print results
[print(row) for row in cur.fetchall()]

