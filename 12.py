#!/usr/bin/python
#-*- coding: utf-8 -*-
#�ж�101-200֮���ж��ٸ��������������������. �ж������ķ�������һ�����ֱ�ȥ��2��sqrt(�����)������ܱ����������������������������֮�������� 
h=0
leap=1
from math import sqrt
from sys import stdout
for i in range (101,200):
    j=int(sqrt(i))
    for k in range (2,j+1):
	    if i%k==0:
		    leap = 0
		    break
    if leap == 1:
	    print ('%-4d' %i)
	    h+=1
	    if h%10 == 0:
		    print (" ")
    leap = 1
print ("the total is %d" %h)
