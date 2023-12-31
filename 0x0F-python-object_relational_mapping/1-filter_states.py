#!/usr/bin/python3
"""
This is a module for mysqldb
"""
import MySQLdb
import sys


if __name__ == '__main__':
    argv = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE 'N%' \
                 ORDER BY states.id ASC")
    states = cur.fetchall()
    for rows in states:
        print(rows)
    cur.close()
    db.close()
