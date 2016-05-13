# -*- coding: utf-8 -*-
# @Date    : 2016
# @Author  :  
# @Link    :  
# @Version :
# @DOM XSS CHECK   https://github.com/ajinabraham/Static-DOM-XSS-Scanner
# @XSS scanner     https://github.com/razielb/xss_scanner
# @XSS scanner     https://github.com/v0mit/PyXSSer
# @XSS scanner     


# notice: 在数据库中取出url的时候，需要对url进行过滤之后再进行检测。（主要是过滤没有参数的地址，因为不存在漏洞）
# .css.jpg.jpeg.gif.png.js
import requests
import re

urls = [
	'http://192.168.204.242/cms/index.php',
	'http://192.168.204.242/cms/admin/',
	'http://192.168.204.242/cms/show.php?id=32',
	'http://192.168.204.242/cms/show.php?id=33',
	'http://192.168.204.242/cms/show.php?id=34',
	'http://192.168.204.242/cms/show.php?id=35',
	'http://192.168.204.242/cms/list.php?id=22',
	'http://192.168.204.242/cms/list.php?id=23',
	'http://192.168.204.242/cms/message.php',
	'http://192.168.204.242/cms/notice.php?id=10',
	'http://192.168.204.242/cms/list.php?id=16'
]

payload = [


]
root_url = "http://192.168.204.242/cms/index.php"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
timeout = 3
r = requests.get(root_url,headers=headers,timeout=timeout)
if r.status_code == requests.codes.ok:
	data = r.text
	forms = re.findall("""<form.*?action=['|"](.*?)['|"].*?method=['|"](.*?)['|"].*?>(.*?)</form>""", data, re.DOTALL)
	print forms


        



class xss_check(object):

	def __init__(self):
		pass


	def get_xss_check(self,url):
		pass


	def post_xss_check(self,url,data):
		pass


	def xss_check(self,method,url):

		if method == 'GET':
			get_xss_check(url)

		elif method == 'POST':
			post_xss_check(url)

		else:
			return 