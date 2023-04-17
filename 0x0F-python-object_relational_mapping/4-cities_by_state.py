#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def list_cities(username, password, database):
    with MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8"
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC"""
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)
    list_cities(argv[1], argv[2], argv[3])
