#!/usr/bin/python3
import MySQLdb
import sys

username, password, database = sys.argv[1:]

with MySQLdb.connect("localhost", username, password, database) as db:
    db.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    results = db.fetchall()

for row in results:
    print(row)

