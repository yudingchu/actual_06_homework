#!/usr/bin/env python 
#-*- coding:utf-8 -*-

File_name = "www_access_20140823.log"
new_file = File_name + ".new"



def gendict(f):
	p_list = []
	p_dict = {}
	for p_line in f:
		n_line = [p_line.split()[i] for i in (8,6,0)]
		p_list.append(n_line)
	p_list = [tuple(x) for x in p_list]
	for i in p_list:
		p_dict[i] = p_dict[i] + 1 if i in p_dict else 1
	return p_dict
#d -> dict n -> top n

def sort_dict(d,n):
	lst = d.items()
	for i in xrange(n):
		min_index = i
		for j in xrange(i+1,len(lst)):
			if lst[min_index][1] < lst[j][1]:
				min_index = j
		lst[i],lst[min_index] = lst[min_index],lst[i]
	return lst[:n]

def write_list(f,l):
	for i in l:
		lst = list(i)
		line = str(lst) + '\n'
		f.writelines(line)


with open(File_name,"r") as file_process:
	with open(new_file,"a+") as file_gen:
		p_dict = gendict(file_process)
		sort_lst = sort_dict(p_dict,5)
		write_list(file_gen,sort_lst)








