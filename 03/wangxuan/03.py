#!/usr/bin/env python

import re 
from collections import Counter

input_str = '''Take me to your heart take me to your soul hold give me your hand before I'm old.'''
list_str = re.findall(r'\w+',input_str)
dict_str = {}
for i in list_str:
	dict_str[i] = dict_str[i]+1 if i in dict_str else 1

def insert_sort(l):
	for i in range(len(l)):
		min_index = i
		for j in range(i+1,len(l)):
			if l[min_index][1] < l[j][1]:
				min_index = j
		l[i],l[min_index] = l[min_index],l[i]
	return l	
sort_str =  insert_sort(dict_str.items())
for i in range(10):
	print sort_str[i]
