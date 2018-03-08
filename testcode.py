#!/usr/bin/env python
# _*_ coding:utf-8 _*_
name_list = ['a', 'b', 'c', 'd', 'b', 'b', 'c', 'b']
X ='b'
name_list.count(X)
jieshou = []
old_index = 0
for i in range(name_list.count(X)):
    new_list = []
    new_list = name_list[old_index:]
    new_index = new_list.index(X)
    jieshou.append(new_index+old_index)
    old_index = new_index+old_index+1
else:
    print jieshou