#!/usr/bin/python3
"""
lists all cities from the database
"""
import MySQLdb
import sys

con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                      passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = con.cursor()
cur.execute("""SELECT cities.name
               FROM cities
               LEFT JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC""", (sys.argv[4],))
rows = cur.fetchall()
print(", ".join([row[0] for row in rows]))
cur.close()
con.close()
