#_*_coding:utf-8_*_

from sqlite3worker import Sqlite3Worker
import logging
logging.basicConfig()


class HtmlOutputer(object):

	def __init__(self):
		self.urls = set()
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return

		self.datas.append(data)

	def collect_urls(self,urls):
		if urls is None:
			return
		self.urls = self.urls | urls

	def insert_get_data(self):

		sql_worker = Sqlite3Worker("../config/spiderurls.db")
		sql_worker.execute("DROP TABLE IF EXISTS spiderurls")
		sql_worker.execute("CREATE TABLE IF NOT EXISTS spiderurls( \
					id INTEGER PRIMARY KEY, \
					url TEXT \
					)")
		
		for url in self.urls:
			sql_worker.execute("INSERT INTO spiderurls (url) VALUES (?) ",(url,))
		sql_worker.close()

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
