#!/usr/bin/env python
import time

time1 =time.time()
result_list = []
url_dict = {}
try:
	f = open('www_access_20140823.log')
	for line in f.readlines():
		tmp_list = line.replace('\n','').split()
		ip = tmp_list[0]
		url = tmp_list[6]
		http_statu = tmp_list[8]
		tmp_key = (ip,url,http_statu)
		if tmp_key not in url_dict:
			url_dict[tmp_key] = 1
		else:
			url_dict[tmp_key] = url_dict[tmp_key] + 1
	f.close()
	tmp_value_list = url_dict.values()
	tmp_value_list.sort()
	maxs = tmp_value_list[len(tmp_value_list)-10:]
	for k,v in url_dict.items():
		if v in maxs:
			ip = k[0]
			url = k[1]
			http_statu = k[-1]
			tmp_list = [http_statu,url,(ip,v)]
			result_list.append(tmp_list)
	for i in result_list:
		print i
	time2 = time.time()
	print time2 - time1
except IOError:
	print 'The file is not exsit!'
