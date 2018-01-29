#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：使用lambda来创建匿名函数。
#use of _name__='__main__'
maximum = lambda x,y: ((x>y)*x+(x<y)*y)
def main():

	a=10
	b=20
	print ("the larger one is %d" % maximum(a,b))
if __name__ == '__main__':
	main()
	print (" hello ")
