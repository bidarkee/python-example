#!/usr/bin/env python
#-*- coding: utf-8 -*-
#通过urllib(2)模块下载网络内容
import urllib,urllib2,gevent
#引入正则表达式模块，时间模块
import re,time
from gevent import monkey
   
monkey.patch_all()
   
def geturllist(url):
    url_list=[]
    print url       
    #user_agent = 'Mozilla/5.5 (compatible; MSIE 5.5; Windows NT)'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    values = {'name' : 'Michael Foord',
              'location' : 'Northampton',
		'language' : 'Python' }
    headers = {'User-Agent':user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(url,headers=headers)
    s = urllib2.urlopen(req)
    text = s.read()
    #正则匹配，匹配其中的图片
    html = re.search(r'<ol.*</ol>', text, re.S)
    #urls = re.finditer(r'<p><img src="(.+?)jpg" /></p>',html.group(),re.I)
    #urls = re.finditer(r'img src="(.+?)jpg" /></p>',html.group(),re.I)
    urls = re.finditer(r'<p><a href="(.+?)jpg" target',html.group(),re.I)
#    print urls
    for i in urls:
	#print i
        url=i.group(1).strip()+str("jpg")
	print url
        url_list.append(url)
    return url_list
   
def download(down_url):
    name=str(time.time())[:-3]+"_"+re.sub('.+?/','',down_url)
    print name
    print down_url
    user_agent = 'Mozilla/5.5 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    req = urllib2.Request(down_url,headers=headers)
    f = urllib2.urlopen(req)
    with open(name,"wb") as code:
    	code.write(f.read())
    
    #urllib.urlretrieve(down_url, "./"+name)
   
def getpageurl():
    page_list = []
    #进行列表页循环
    for page in range(1005,1805):
        #url="http://jandan.net/ooxx/page-"+str(page)+"#comments"
	url="http://jandan.net/ooxx/page-"+str(page)+"#comments"
        #把生成的url加入到page_list中
        page_list.append(url)
    return page_list
if __name__ == '__main__':
    jobs = []
    pageurl = getpageurl()[::-1]
    #进行图片下载
    for i in pageurl:
        for (downurl) in geturllist(i):
            jobs.append(gevent.spawn(download, downurl))
    gevent.joinall(jobs)
