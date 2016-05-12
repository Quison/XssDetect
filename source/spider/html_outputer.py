#_*_coding:utf-8_*_

from sqlite3worker import Sqlite3Worker
import sqlite3

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
#		print "sssssssssssssssssss"

	def insert_get_data(self):
		conn = sqlite3.connect('spiderurls.db')
		cursor = conn.cursor()
#		cursor.execute("CREATE TABLE spiderurls (id INTEGER, method TEXT, url TEXT, data TEXT)")
		for url in self.urls:
			count = 1 
			cursor.execute("INSERT INTO spiderurls VALUES (count,'GET',url,'dingdong')")
			count = count + 1
		cursor.close()
		conn.commit()
		conn.close()
#		sql_worker = Sqlite3Worker('spiderurls.db')
#		sql_worker.execute("CREATE TABLE spiderurls (id INTEGER, method TEXT, url TEXT, data TEXT)")
#		print self.urls
#		for url in self.urls:
#			count = 1 
#			sql_worker.execute("INSERT INTO spiderurls VALUES (count,'GET',url,"")")
#			count = count + 1


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
