#! /usr/bin/env python   
# -*- coding: utf-8 -*- 

File_name = "www_access_20140823.log"
new_file = File_name + ".new"
print new_file

def process_line(line):
	n_line = [p_line.split()[i] for i in (8,6,0)]
	p_list.append(n_line)
#	for i in p_list:	
#		p_dict[i] += 1 if i in p_dict else 1
	return p_list



p_list = []
p_dict = {}
w_line = []
with open(File_name,"r") as file_process:
	with open(new_file,"a+") as file_gen:
		for p_line in file_process:
			process_line(p_line)
		p_list = [tuple(x) for x in p_list]
		for i in p_list:
			p_dict[i] = p_dict[i]+1 if i in p_dict else 1
		for i,j in p_dict.items():
			n_line= list(i[0:2])
		#	t = (i[2],j)
			n_line.append((i[2],j))
			n_line = [str(n_line),"\n"]
			file_gen.writelines(n_line)




