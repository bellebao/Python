#!/usr/bin/python
# -*- coding: UTF-8 -*-

#��Ŀ����s=a+aa+aaa+aaaa+aa...a��ֵ������a��һ�����֡�����2+22+222+2222+22222(��ʱ����5�������)������������ɼ��̿��ơ�
from functools import reduce
Tn = 0
Sn =[]
S = 0
n= int(input("n=:\n"))
a = int(input("a=:\n"))
for count in range (n):
	Tn=Tn + a
	a = a* 10
	Sn.append(Tn)
	print (Tn, end="+")

S = reduce(lambda x,y: x+y, Sn)
print ("0=%d" %S)

#reduce(function, sequence, starting_value)����sequence�е�item˳���������function�������starting_value����������Ϊ��ʼֵ���ã��������������List��ͣ�
#>>> def add(x,y): return x + y 
#>>> reduce(add, range(1, 11)) 
#55 ��ע��1+2+3+4+5+6+7+8+9+10��
#>>> reduce(add, range(1, 11), 20) 
#75 ��ע��1+2+3+4+5+6+7+8+9+10+20��

#lambda������Python֧��һ����Ȥ���﷨������������ٶ��嵥�е���С������������C�����еĺ꣬��Щ����lambda�ĺ������Ǵ�LISP�������ģ����������κ���Ҫ�����ĵط��� 
#>>> g = lambda x: x * 2 
#>>> g(3) 
#6 
#>>> (lambda x: x * 2)(3) 
#6
