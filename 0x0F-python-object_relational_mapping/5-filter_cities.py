#!/usr/bin/python3
"""
This is a module for mysqldb
"""
import MySQLdb
import sys


if __name__ == '__main__':
    argv = sys.argv
    if (len(argv) != 5):
        print("Usage: Arguments must be four!")
        sys.exit(1)

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    state_name = argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                   FROM cities\
                  WHERE cities.state_id = %s.id\
                  ORDER BY cities.id ASC", (state_name,))
    cities = cur.fetchall()
    print(cities)
    cur.close()
    db.close()
