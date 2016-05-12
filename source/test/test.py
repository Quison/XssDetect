#_*_coding:utf-8_*_

'''
{   "server":"159.203.227.16",
    "server_port":18388,
    "local_port":1080,
    "password":"wRkG4KqH",
    "timeout":600,
    "method":"chacha20"
 }

^(http(s)?://)?([\w-]+\.)+[\w-]+/?

www.baidu.com
192.168.1.1
http://192.168.1.1/inde.php?id=1
http://www.baidu.com/inde.php?id=1
http://www.baidu.com/inde.php

'''

import re

m = re.match(r"^(http(s)?://)?([\w-]+\.)+[\w-]+/?","http://192.168.1.1/inde.php?id=1",re.M|re.I).group()

print m
