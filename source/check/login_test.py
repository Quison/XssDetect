# -*- encoding: utf-8 -*-
import requests
import urlparse
from lxml import etree
import sys
sys.path.append(r"../comm")

import authentication_login

import requests, re, urllib, random, string, urllib2
root_url = "http://127.0.0.1/cms/admin/menu.php"
r = authentication_login.LOGIN_SESSION.get(root_url)
html_cont = r.content
print html_cont