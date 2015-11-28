try:
	src_file = open('www_access_20140823.log')
except IOError:
	print 'file not exist!'
else:
	lines = src_file.readlines()
	data = []
	count = {}
	count_times_sort=[]
	top_10 = []
	write_to_file=[]
	for line in lines:
		data = line.split(' ')
		key = tuple([data[8],data[6],data[0]])
		count[key] = count.setdefault(key,0) + 1
	for key in count:
		if count[key] not in count_times_sort:
			count_times_sort.append(count[key])
	for loop in range(len(count_times_sort) - 1):
		for num in range(len(count_times_sort) - 1 - loop):
			if count_times_sort[num] < count_times_sort[num + 1]:
				count_times_sort[num],count_times_sort[num + 1] = count_times_sort[num + 1],count_times_sort[num]
	for num in count_times_sort:
		if len(top_10) < 10:
			for key in count:
				if count[key] == num:
					top_10.append([key,count[key]])
		elif len(top_10) >= 10:
			break
	print top_10
	print len(top_10)
	for num in range(len(top_10) - 1):
		write_to_file.append(str(top_10[num]) + '\n')
	write_to_file.append(str(top_10[-1]))
	print write_to_file
	des_file = open('abc.txt','a+')
	des_file.writelines(write_to_file)
	des_file.close()
