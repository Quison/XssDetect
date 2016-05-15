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


def _retrieve_content(url, data=None):
    try:
        req = urllib2.Request("".join(url[i].replace(' ', "%20") if i > url.find('?') else url[i] for i in xrange(len(url))), data, _headers)
        retval = urllib2.urlopen(req, timeout=TIMEOUT).read()
    except Exception, ex:
        retval = ex.read() if hasattr(ex, "read") else getattr(ex, "msg", str())
    return retval or ""

def _contains(content, chars):
    #re.escape(string)  对字符串中的非字母数字进行转义
    content = re.sub(r"\\[%s]" % re.escape("".join(chars)), "", content) if chars else content
    return all(char in content for char in chars)


url = "http://127.0.0.1/cms/index.php?id=123&p=0009#qwe"

wwww = re.sub(r"=(&|\Z)", "=1\g<1>", url) if url else url
print wwww