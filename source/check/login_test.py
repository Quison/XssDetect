# -*- encoding: utf-8 -*-
import requests
import sys
sys.path.append(r"../comm")

import authentication_login

import requests, re, urllib, random, string, urllib2

print authentication_login.LOGIN_SESSION
r = authentication_login.LOGIN_SESSION.get("http://127.0.0.1/cms/admin/index.php")
print r.text




