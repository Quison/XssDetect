# -*- encoding: utf-8 -*-

import redis

from pybloom import BloomFilter
f = BloomFilter(capacity=1000, error_rate=0.001)

for x in xrange(1,5):
	f.add(x)

for y in xrange(3,7):
	if y in f:
		pass
	else:
		f.add(y)

for w in xrange(1,9):
	if w in f:
		print 'true: %s' %w
	else:
		print w

r = redis.Redis(host='localhost',port=6379,db=0)
#r = redis.StrictRedis(host='localhost', port=6379, db=0)
for x in xrange(1,10):
	key='foo'+ str(x)
	r.set(key,x)

r.set('123','erq')    # 设置一个键值对
print r.get('foo1')   # 获取某key的值
print r.delete('123')  #删除某key的value
print r.dbsize()  # 数据库大小
r.save()   #强行把数据库保存到硬盘。保存时阻塞 返回ture
r.flushdb()   #删除当前数据库的所有数据  返回ture
print r.keys()   # 列出所有键值。