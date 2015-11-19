#!/usr/bin/python 
#-*- coding:utf8  -*-

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import time

def fetch(pid):
    response = urllib2.urlopen('http://www.baidu.com')
    result = response.read()

    print result[:60]

def synchronous():
    start  = time.clock()

    for i in range(1,30):
        fetch(i)

    end = (time.clock()-start)
    print("synchronous time used:",end)

def asynchronous():
    start  = time.clock()

    threads = []
    for i in range(1,30):
        threads.append(gevent.spawn(fetch,i))

    gevent.joinall(threads)
    end = (time.clock()-start)
    print("asynchronous time used:",end)


print 'synchronous:'
synchronous()

print 'asynchronous:'
asynchronous()
