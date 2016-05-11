#! /usr/bin/env python
#_*_coding:utf-8_*_

class HtmlOutputer(object):

	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return

		self.datas.append(data)

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
