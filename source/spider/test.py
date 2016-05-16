# -*- coding: cp936 -*-
import urllib,urllib2,sgmllib,os
import time,threading,Queue,re,sys,StringIO,gzip

class URLList(sgmllib.SGMLParser):
    def reset(self):
        sgmllib.SGMLParser.reset(self)
        #maxsize < 1 表示无穷队列
        self.URLqueue = Queue.Queue(maxsize = -1)
        
    def start_a(self,attrs):
        href = [v for k,v in attrs if k == 'href']
        if href:
            for u in href:
                #判断URL是不是正确的
                pat = re.compile(r'http://(.+?)')
                if len(re.findall(pat,u)) == 0:
                    continue        
                self.URLqueue.put(u)

class spider(threading.Thread):
    def __init__(self,name,parser,dicPath = os.path.abspath(os.path.dirname(sys.argv[0]))+"\\page_downloads"):
        threading.Thread.__init__(self)
        self.name = name
        self.parser = parser
        self.pageCount = 0
        self.dicPath = dicPath+"\\"+name
        self.TIMEOUT = 10        
    def run(self):
        #创建一个downloads文件夹放置下载的pages
        if os.path.exists(self.dicPath) == False :
            os.mkdir(self.dicPath)
        opener = urllib2.build_opener()
        #共用URLList的URLqueue，如果队列为空有两种情况
        #一种是没有可抓取的URL了，第二种是在等待线程抓ing
        #这里默认为第二种情况，当队列为空超过TIMEOUT，就判定为结束    
        start = time.clock()
        end = time.clock()
        while True:
            if self.parser.URLqueue.empty() == False:
                start = time.clock()
                
                url = self.parser.URLqueue.get()
                print self.name + ": "+url
                #用gzip的方式下载网页，提高速度
                request = urllib2.Request(url)
                request.add_header('Accept-encoding','gzip')
                try:
                    page = opener.open(request)
                    if page.code == 200:
                        predata = page.read()
                        pdata = StringIO.StringIO(predata)
                        gzipper = gzip.GzipFile(fileobj = pdata)
                        try:
                            data = gzipper.read()
                        except:
                            #如果服务器不支持gzip，那么就直接下载网页
                            data = predata
                        try:
                            self.parser.feed(data)
                        except Exception as e:
                            print "页面分析不了: "+str(e)
                        try:
                            filePath = self.dicPath+"\\"+str(self.pageCount)+".html"
                            self.pageCount += 1
                            file = open(filePath,'w')
                            file.write(data)
                            file.close()
                        except:
                            print "文件写错误"
                except Exception as e:
                    print "请求错误: "+str(e)
            else:
                #如果空队列这种状态保持TIMEOUT秒，就退出
                end = time.clock()
                if end - start > self.TIMEOUT:
                    break
                                
thCnt = 2
thList = []
startURL = "http://www.baidu.com"
parser = URLList()
URLdata = urllib.urlopen(startURL)
parser.feed(URLdata.read())
URLdata.close()

for i in range(thCnt):
    th = spider('th'+str(i),parser)
    thList.append(th)
for t in thList:
    t.start()

for t in thList:
    t.join()
print "处理结束"
