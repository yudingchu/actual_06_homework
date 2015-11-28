#coding:utf-8

http_list = []
nginx_dict = {}

#读取文件
nginxFile = file('www_access_20140823.log','r')
nginxFileLines = nginxFile.xreadlines()
for i in nginxFileLines:
	nginxFileLine = i.split(' ')
	#截取http内容的IP,url,code信息
	http_ip,http_url,http_code = nginxFileLine[0],nginxFileLine[6],nginxFileLine[8]
	#把截取的http内容整合成一个列表
	http_list.append([http_code,http_url,http_ip])

#对http列表转换成字典并且进行分类统计
for i in http_list:
	t_i = tuple(i)
	if t_i not in nginx_dict:
		nginx_dict[t_i] = 1
	else:
		nginx_dict[t_i] += 1

#对http字典的内容排序并且按要求输出
analyse_result_sorted = sorted(nginx_dict.items(),key=lambda x:x[1],reverse=True)

for i in analyse_result_sorted:
	print [i[0][0],i[0][1],(i[0][2],i[1])]

#关闭文件
nginxFile.close()