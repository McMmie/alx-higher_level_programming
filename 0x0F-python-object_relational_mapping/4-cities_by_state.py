#!/usr/bin/python3
"""
This is a module for mysqldb
"""
import MySQLdb
import sys


if __name__ == '__main__':
    argv = sys.argv
    if (len(argv) != 4):
        sys.exit(1)

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities\
                 JOIN states\
                 WHERE cities.state_id = states.id\
                 ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for rows in cities:
        print(rows)
    cur.close()
    db.close()
