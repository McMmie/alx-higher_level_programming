#!/usr/bin/python3
"""
This is a module for mysqldb
"""
import MySQLdb
import sys


argv = sys.argv
db = MySQLdb.connect(host=LOCALHOST, port=3306, user=argv[0], passwd=argv[1], db=argv[2])
cur = db.cursor()
cur.execute("SELECT * from states")
states = cur.fetchall()
print(states)
cur.close()
db.close()
