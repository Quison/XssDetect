# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(r"../comm")
import wx
from sqlite3worker import Sqlite3Worker

import requests, re, urllib, random, string, urllib2
import authentication_login

import json,urllib

'''
re.sub(pattern, repl, string, max=0) 以正则为基础，在string中，把pattern替换成repl
re.sub('[abc]', 'o', 'Mark')--》'Mork'  。
str.replace(old, new[, max]) 把字符串中的 old 替换成 new ，替换不超过 max 次。
re.finditer(pattern, string, flags=0) 返回一个迭代器,可以一个一个的得到匹配返回的 Match对象。这在对每次返回的对象进行比较复杂的操作时比较有用。
re.search(pattern, string, flags=0) 扫描整个字符串并返回第一个成功的匹配。 re.I 使匹配对大小写不敏感
re.escape(string) 对字符串中的非字母数字进行转义
strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
'''

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
					# tampered 是把上面获取的参数进行替换，domain+参数+[']前缀+随机pool+后缀，最后吧所有参数都url编码 # eg: ?page=8890%27tnmow%3C%3E%27%3B%22ukenc&id=34#at123 （?page=8890'tnmow<>';"ukenc&id=34#at123）
					tampered = current.replace(match.group(0), "%s%s" % (match.group(0), "%s%s%s%s" % ("'" if pool == LARGER_CHAR_POOL else "", prefix, "".join(random.sample(pool, len(pool))), suffix)))
					content = self._retrieve_content(url, tampered).replace("%s%s" % ("'" if pool == LARGER_CHAR_POOL else "", prefix), prefix) if data else self._retrieve_content(tampered, data)
					#print content # 获取攻击之后的源码content
					for sample in re.finditer("%s([^ ]+?)%s" % (prefix, suffix), content, re.I):
						for regex, condition, info, content_removal_regex in REGULAR_PATTERNS:	 #这里循环输出REGULAR_PATTERNS规律，进行匹配相关字段
							# 使用正则 \A[^<>]*%(chars)s[^<>]*\Z  合并chars(rdjeo\;\"\>\<\'gqejn)之后，进行对返回源进行匹配eg: \A[^<>]*tnmow\;\"\>\<\'ukenc[^<>]*\Z
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
