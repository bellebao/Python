# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:49:49 2018

@author: E435157
"""


def extendlist(val, list=[]):
    list.append(val)
    return list

list1 = extendlist(10)
list2=extendlist(123, [])
list3=extendlist('a')

print (list1)
print (list2)
print (list3)