#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：模仿静态变量的用法。
class Static:
	staticVar=5
	def varfunc(self):
		self.staticVar += 1
		print (self.staticVar)

print (Static.staticVar)
a=Static()
for i in range(3):
	a.varfunc()
