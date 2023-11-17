#!/usr/bin/python3
"""
This is a module for mysqldb
"""
import MySQLdb
import sys


if __name__ == '__main__':
    argv = sys.argv
    i = 0
    state_name = argv[4]
    
    if (len(argv) != 5):
        print("Usage: Arguments must be four!")
        sys.exit(1)

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                   FROM cities\
                  WHERE cities.state_id = (SELECT id\
                                             FROM states\
                                            WHERE name = %s)\
                  ORDER BY cities.id ASC", (state_name,))
    cities = cur.fetchall()
    for rows in cities:
        for content in rows:
            if i in range(len(cities) - 1):
                print(content, end=', ')
                i += 1
            else:
                print(content)
    cur.close()
    db.close()
