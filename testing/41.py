#!/usr/bin/python
# -*- coding: UTF-8 -*-

#��Ŀ��ģ�¾�̬�������÷���
class Static:
	staticVar=5
	def varfunc(self):
		self.staticVar += 1
		print (self.staticVar)

print (Static.staticVar)
a=Static()
for i in range(3):
	a.varfunc()
