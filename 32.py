#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：按相反的顺序输出列表的值

a = ["one", "two", "three"]
for i in a[::-1]:
	print (i)

a.reverse()

print (a)

#常用列表操作方法

#list.append():追加成员

#list.count(x):计算列表中参数x出现的次数

#list.extend(L):向列表中追加另一个列表L

#list.index(x):获得参数x在列表中的位置

#list.insert():向列表中插入数据

#list.pop():删除列表中的成员（通过下标删除）

#list.remove():删除列表中的成员（直接删除）

#list.reverse():将列表中成员的顺序颠倒

#list.sort():将列表中成员排序
