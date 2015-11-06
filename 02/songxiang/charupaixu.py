num_list = [99999,99999,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for i in range(1,len(num_list)):
	for j in range(i)[::-1]:
		if num_list[j]>num_list[j+1]:
			num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
print num_list