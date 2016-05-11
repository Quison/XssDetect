# -*- encoding: utf-8 -*-

import sqlite3
from sqlite3worker import Sqlite3Worker

'''
sql_worker = Sqlite3Worker('test.db')
sql_worker.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
sql_worker.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
sql_worker.execute("INSERT INTO stocks VALUES ('2007-01-05','BUY','RHAT',100,35.14)")

result = sql_worker.execute("select date from stocks")
print type(result)

'''

l = [1,2,3,4,5,6,7,8]
s = set(l)
print s
print type(s)
if 3 in s:
	print "in"