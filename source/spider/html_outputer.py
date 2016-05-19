#_*_coding:utf-8_*_

from sqlite3worker import Sqlite3Worker
import logging
logging.basicConfig()


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

	def write_date(self, spider_url_set):
		if spider_url_set is None:
			return
		for spider_url in spider_url_set:
			self.sql_worker.execute("INSERT INTO spiderurls (url, depth, method, param) VALUES (?,?,?,?) ",
				(spider_url.get_url(), spider_url.get_depth(), spider_url.get_method(), spider_url.get_param()))

	def close_sql_worker(self):
		self.sql_worker.close()

	def output_html(self):
		with open('output.html','w') as fout:
			fout.write("<html>")
			fout.write("<body>")
			fout.write("<table>")
			fout.write("<td>name</td>")
			fout.write("<td>score</td>")
			fout.write("<td>year</td>")
			fout.write("<td>url</td>")	
			for data in self.datas:
				fout.write("<tr>")
				fout.write("<td>%s</td>" % data['name'])
				fout.write("<td>%s</td>" % data['score'])
				fout.write("<td>%s</td>" % data['year'])
				fout.write("<td>%s</td>" % data['url'])			
				fout.write("</tr>")
			fout.write("</table>")
			fout.write("</body>")
			fout.write("</html>")
