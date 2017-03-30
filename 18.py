#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
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

#reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和：
#>>> def add(x,y): return x + y 
#>>> reduce(add, range(1, 11)) 
#55 （注：1+2+3+4+5+6+7+8+9+10）
#>>> reduce(add, range(1, 11), 20) 
#75 （注：1+2+3+4+5+6+7+8+9+10+20）

#lambda：这是Python支持一种有趣的语法，它允许你快速定义单行的最小函数，类似与C语言中的宏，这些叫做lambda的函数，是从LISP借用来的，可以用在任何需要函数的地方： 
#>>> g = lambda x: x * 2 
#>>> g(3) 
#6 
#>>> (lambda x: x * 2)(3) 
#6
