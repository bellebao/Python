#!/usr/bin/python
# -*- coding: UTF-8 -*-
#��Ŀ����һ���������ֽ������������磺����90,��ӡ��90=2*3*3*5��
from math import sqrt
def reduceNum(n):
	print ("{}= ".format(n),end="")
	if not isinstance(n, int) or n<=0:
		print ("insert a right num!")
		exit(0)
	elif n in [1]:
		print ("{}=".format(n)),
	while n not in [1]:
		for index in range(2, int(n+1)):
			if n% index ==0:
				n/=index
				if n==1:
					print (index)				
				else :
					print ('{} * '.format(index),end="")
				break	

reduceNum(90)
reduceNum(100)
