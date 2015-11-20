try:
	f = open('www_access_20140823.log')
except IOError:
	print 'file not exist!'
else:
	lines = f.readlines()
	count = {}
	top_10 = []
	for line in lines:
		result = line.split(' ')
		key = tuple([result[8],result[6],result[0]])
		count[key] = count.setdefault(key,0) + 1
	for key in count:
		top_10.append([key,count[key]])
		for num in range(len(top_10)):
			if top_10[-1][1] >= top_10[num][1]:
				top_10.insert(num,top_10.pop())
				break		
	for num in range(10,len(top_10)):
		if top_10[num][1] != top_10[9][1]:
			top_10 = top_10[:num]
			break
	print top_10
