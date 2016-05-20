#_*_coding:utf-8_*_
import urllib, urllib2, re

"""Sqlite thread safe object.

Example:
    from sqlite3worker import Sqlite3Worker
    sql_worker = Sqlite3Worker("/tmp/test.sqlite")
    sql_worker.execute(
        "CREATE TABLE tester (timestamp DATETIME, uuid TEXT)")
    sql_worker.execute(
        "INSERT into tester values (?, ?)", ("2010-01-01 13:00:00", "bow"))
    sql_worker.execute(
        "INSERT into tester values (?, ?)", ("2011-02-02 14:14:14", "dog"))
    sql_worker.execute("SELECT * from tester")
    sql_worker.close()
"""


# 为什么有出冲突了