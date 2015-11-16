#-*- coding: utf-8 -*-

f = open('www_access_20140823.log','r')
whole_list = f.readlines()
f.close()
#  读取文件
d = {}
#  存IP和访问次数
fnew = open('copy.log','a+')
final_list=''
count=0
for i in whole_list:
	new=['']*3
	sigle_list=i.split(' ')
	new[0]=sigle_list[8]
	#http状态
	new[1]=sigle_list[6]
	#访问url
	if sigle_list[0] in d:
		d[sigle_list[0]]=d[sigle_list[0]]+1
	else:
		d[sigle_list[0]]=1
	new[2]=(sigle_list[0],d[sigle_list[0]])
	#ip,访问次数
	newstr = str(new)
	final_list=final_list+newstr+'\n'

fnew.writelines(final_list)
fnew.close()