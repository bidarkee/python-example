#!/usr/bin/python
#-*- coding:utf8 _*_

import gevent
import random

def task(pid):
	#gevent.sleep(random.randint(0,2)*0.001)
	gevent.sleep(1)
	print('Task',pid,'done')

def synchronous():
	for i in range(1,10):
		task(i)

def asynchronous():
	threads  = [gevent.spawn(task,i,3) for i in range(1,10)]
	gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()

