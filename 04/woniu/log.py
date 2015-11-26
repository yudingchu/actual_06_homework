f = open('../songxiang/www_access_20140823.log')
res = {}
for l in f:
	arr = l.split(' ')
	ip,url,status = arr[0],arr[6],arr[8]
	res[(ip,url,status)] = res.get((ip,url,status),0)+1
sort_list = sorted([(k[0],k[1],k[2],v) for k,v in res.items()],key=lambda x:x[3],reverse=True)
for i in range(len(sort_list)):
	if i>10 and sort_list[i][3]>sort_list[i+1][3]:
		break
	print sort_list[i]