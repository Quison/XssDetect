# -*- encoding: utf-8 -*-
import requests
import urllib
import urllib2


'''
def _retrieve_content(url, data=None):
	# 把url里面的空格进行urlencode
	new_url = "".join(url[i].replace(' ', "%20") if i > url.find('?') else url[i] for i in xrange(len(url)))
	#data = urllib.urlencode(data) if data else ""
	try:
		req = urllib2.Request(new_url, data)
		retval = urllib2.urlopen(req).read()
	except Exception, ex:
		retval = ex.read() if hasattr(ex, "read") else getattr(ex, "msg", str())
	return retval or ""
'''
#&image.x=68&image.y=37
#data = {"username":"admin","password":"123456"}
data = "username=admin&image.x=68&image.y=37&password=123456"
url = "http://192.168.204.242/cms/admin/login.action.php"
s = requests.Session()
s.post(url,data=data)
print r.text 


q = _retrieve_content(url,data)
print q

