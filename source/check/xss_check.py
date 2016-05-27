# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(r"../comm")
import wx
from sqlite3worker import Sqlite3Worker

import requests, re, urllib, random, string, urllib2
import authentication_login

import json,urllib

PREFIX_SUFFIX_LENGTH = 5
SMALLER_CHAR_POOL = ('<', '>')
LARGER_CHAR_POOL = ('\'', '"', '>', '<', ';')
GET, POST = "GET", "POST"

DOM_FILTER_REGEX = r"(?s)<!--.*?-->|\bescape\([^)]+\)|\([^)]+==[^(]+\)|\"[^\"]+\"|'[^']+'"
DOM_PATTERNS = (
    r"(?s)<script[^>]*>[^<]*?(var|\n)\s*(\w+)\s*=[^;]*(document\.(location|URL|documentURI)|location\.(href|search)|window\.location)[^;]*;[^<]*(document\.write(ln)?\(|\.innerHTML\s*=|eval\(|setTimeout\(|setInterval\(|location\.(replace|assign)\(|setAttribute\()[^;]*\2.*?</script>",
    r"(?s)<script[^>]*>[^<]*?(document\.write\(|\.innerHTML\s*=|eval\(|setTimeout\(|setInterval\(|location\.(replace|assign)\(|setAttribute\()[^;]*(document\.(location|URL|documentURI)|location\.(href|search)|window\.location).*?</script>",
)

REGULAR_PATTERNS = (
    (r"\A[^<>]*%(chars)s[^<>]*\Z", ('<', '>'), "\".xss.\", pure text response, %(filtering)s filtering", None),
    (r"<!--[^>]*%(chars)s|%(chars)s[^<]*-->", ('<', '>'), "\"<!--.'.xss.'.-->\", inside the comment, %(filtering)s filtering", None),
    (r"(?s)<script[^>]*>[^<]*?'[^<']*%(chars)s|%(chars)s[^<']*'[^<]*</script>", ('\'', ';'), "\"<script>.'.xss.'.</script>\", enclosed by <script> tags, inside single-quotes, %(filtering)s filtering", None),
    (r'(?s)<script[^>]*>[^<]*?"[^<"]*%(chars)s|%(chars)s[^<"]*"[^<]*</script>', ('"', ';'), "'<script>.\".xss.\".</script>', enclosed by <script> tags, inside double-quotes, %(filtering)s filtering", None),
    (r"(?s)<script[^>]*>[^<]*?%(chars)s|%(chars)s[^<]*</script>", (';',), "\"<script>.xss.</script>\", enclosed by <script> tags, %(filtering)s filtering", None),
    (r">[^<]*%(chars)s[^<]*(<|\Z)", ('<', '>'), "\">.xss.<\", outside of tags, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
    (r"<[^>]*'[^>']*%(chars)s[^>']*'[^>]*>", ('\'',), "\"<.'.xss.'.>\", inside the tag, inside single-quotes, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
    (r'<[^>]*"[^>"]*%(chars)s[^>"]*"[^>]*>', ('"',), "'<.\".xss.\".>', inside the tag, inside double-quotes, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
    (r"<[^>]*%(chars)s[^>]*>", (), "\"<.xss.>\", inside the tag, outside of quotes, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
)

class XssCheck(object):

	def __init__(self, login_session):
		
		self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
		self.timeout = 2
		self.login_session = login_session

	#将参数paramter转换成字典格式dict
	def modify_paramter(self,paramter):
		if paramter is None:
			return 
		paramter_dict = {}
		paramter_list = paramter.split('&')
		map(lambda x:paramter_dict.setdefault(x.split('=')[0], x.split('=')[1]), paramter_list)
		return paramter_dict


	# 判断 chars 是否为 content 的子集
	def _contains(self, content, chars):
		content = re.sub(r"\\[%s]" % re.escape("".join(chars)), "", content) if chars else content
		return all(char in content for char in chars)

	# download html
	def _retrieve_content(self,url,data=None):
		data = self.modify_paramter(data)
		try:
			if self.login_session:
				r = self.login_session.post(url,data,timeout=self.timeout,allow_redirects=False) if data else self.login_session.get(url,timeout=self.timeout,allow_redirects=False)
			else:
				r = requests.post(url,data,timeout=self.timeout,allow_redirects=False) if data else requests.get(url,timeout=self.timeout,allow_redirects=False)
			
			return r.content
		except Exception, e:
			return ""


	# dom xss check
	def do_dom_xss_check(self, url, data=None):
		phase = "DOM"
		url = re.sub(r"=(&|\Z)", "=1\g<1>", url) if url else url
		original = re.sub(DOM_FILTER_REGEX, "",self._retrieve_content(url,data))
		dom = max(re.search(_, original) for _ in DOM_PATTERNS)
		if dom:
			yield phase,url,dom.group(0)


	def do_xss_check(self,url,data=None):
		
		self.do_dom_xss_check(url,data)
		phase = "POST" if data else "GET"
		current = data if data else url
		prefix, suffix = ("".join(random.sample(string.ascii_lowercase, PREFIX_SUFFIX_LENGTH)) for i in xrange(2))
		try:
			for match in re.finditer(r"((\A|[?&])(?P<parameter>[\w\[\]]+)=)(?P<value>[^&#]+)", current):
				for pool in (LARGER_CHAR_POOL, SMALLER_CHAR_POOL):
					#tampered = current.replace(match.group(0), "%s%s" % (match.group(0), urllib.quote("%s%s%s%s" % ("'" if pool == LARGER_CHAR_POOL else "", prefix, "".join(random.sample(pool, len(pool))), suffix))))
					tampered = current.replace(match.group(0), "%s%s" % (match.group(0), "%s%s%s%s" % ("'" if pool == LARGER_CHAR_POOL else "", prefix, "".join(random.sample(pool, len(pool))), suffix)))
					content = self._retrieve_content(url, tampered).replace("%s%s" % ("'" if pool == LARGER_CHAR_POOL else "", prefix), prefix) if data else self._retrieve_content(tampered, data)
					#print content
					for sample in re.finditer("%s([^ ]+?)%s" % (prefix, suffix), content, re.I):
						for regex, condition, info, content_removal_regex in REGULAR_PATTERNS:
							context = re.search(regex % {"chars": re.escape(sample.group(0))}, re.sub(content_removal_regex or "", "", content), re.I)
							if context and sample.group(1).strip():
								if self._contains(sample.group(1), condition):
									#print " (i) %s parameter '%s' appears to be XSS vulnerable (%s)" % (phase, match.group("parameter"), info % dict((("filtering", "no" if all(char in sample.group(1) for char in LARGER_CHAR_POOL) else "some"),)))
									yield phase,url,match.group("parameter")
		except KeyboardInterrupt:
			return

	# 自主测试检测函数，界面无调用
	def xss_check_main(self):
		if os.path.exists('../config/spiderurls.db'):
			sql_worker = Sqlite3Worker("../config/spiderurls.db")
		else:
			print "db is not exit"
			return

		results = sql_worker.execute("SELECT method,url,param from spiderurls")
		for method,url,param in results:

#			if method == "GET" or method == "get":
#				yield self.do_xss_check(url)
			if method.lower() == "post":
				if param is None:
					print "post parm is none"
					continue
				data = param
				print method,url,data
				yield self.do_xss_check(url,data)

		sql_worker.close()

'''
if __name__ == '__main__':

	s = requests.Session()

#	url = "http://192.168.204.242/cms/admin/login.action.php"
#	data = {"username":"admin","password":"123456"}
#	datap = "username=admin'/><scRipt>alert(1)</scRipt>&password=123456"
#	r = s.post(url,data,allow_redirects=False)
#	print s.get("http://192.168.204.242/cms/admin/index.php").text

	xss = XssCheck(s)
#	print xss._retrieve_content(url,datap)
	qwe = xss.xss_check_main()
	for x in qwe:
		for xx in x:
			print xx


http://192.168.24.129/cms/admin/login.action.php
username
password
http://192.168.24.129/cms/admin/index.php
'''