#!/bin/env python
#coding:utf-8
l = [(1,4),(5,1),(2,3)]
#级别一： 
sorted(l,key= lambda l: max(l))
#级别二： 
sorted(l,key= lambda l: l[0] if l[0]>l[1] else l[1])