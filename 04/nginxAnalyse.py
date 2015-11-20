#coding:utf-8

http_list = []
nginx_list = []
nginx_result = {}
analyse_result = []

#读取文件
nginxFile = file('www_access_20140823.log','r')
nginxFileLines = nginxFile.readlines()
#关闭文件
nginxFile.close()
for i in nginxFileLines:
	nginxFileLine = i.split(' ')
	#截取http内容的IP信息
	http_ip = nginxFileLine[0]
	#截取http内容的url信息
	http_url = nginxFileLine[6]
	#截取http内容的错误代码信息
	http_code = nginxFileLine[8]
	#把截取的http内容整合成一个列表
	http_list.append([http_code,http_url,http_ip])

#对http列表转换成字典并且进行分类统计
for i in http_list:
	if not i in nginx_list:
		nginx_list.append([i[0],i[1],i[2]])
		t_i = tuple(i)
		nginx_result[t_i] = 1
			
	else:
		t_i = tuple(i)
		nginx_result[t_i] += 1

#对http字典的内容排序并且按要求输出
analyse_result_sorted = sorted(nginx_result.items(),key=lambda x:x[1],reverse=True)

for i in analyse_result_sorted:
	analyse_result.append([i[0][0],i[0][1],(i[0][2],i[1])])

for i in analyse_result:
	print i