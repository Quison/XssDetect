#_*_coding:utf-8_*_

import sys
import logging
logging.basicConfig()
sys.path.append(r"../comm")
from sqlite3worker import Sqlite3Worker


class HtmlOutputer(object):

	def __init__(self):
		self.sql_worker = Sqlite3Worker("../config/spiderurls.db")
		self.sql_worker.execute("DROP TABLE IF EXISTS spiderurls")
		self.sql_worker.execute("CREATE TABLE IF NOT EXISTS spiderurls( \
					id INTEGER PRIMARY KEY, \
					url TEXT, \
					depth INTEGER,\
					method TEXT,\
					param TEXT\
					)")

	def write_date(self, spider_url):
		if spider_url is None:
			return
		self.sql_worker.execute("INSERT INTO spiderurls (url, depth, method, param) VALUES (?,?,?,?) ",
			(spider_url.get_url(), spider_url.get_depth(), spider_url.get_method(), spider_url.get_param()))

	def close_sql_worker(self):
		self.sql_worker.close()
