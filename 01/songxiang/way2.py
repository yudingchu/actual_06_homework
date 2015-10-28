num_list = [99999,99999,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(len(num_list)):
	for j in range(len(num_list)-1-i):
		if num_list[j] > num_list[j+1]:
			num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
max1 = num_list[len(num_list)-1]

for k in range(len(num_list)):
	max2 = num_list[len(num_list)-2-k]
	if max2 != max1:
		break

print 'the biggest is %d, the second biggest is %d ' % (max1,max2)
