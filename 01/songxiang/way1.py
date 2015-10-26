num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1 = int(num_list[0])
max2 = int(num_list[0])
for i in num_list:
	if i > max1:
		max2 = max1
		max1 = i
print 'The biggest is %d , the second is %d ' % (max1,max2)