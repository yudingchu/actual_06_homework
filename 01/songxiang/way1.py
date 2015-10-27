num_list = [99999,99999,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1 = int(num_list[0])
max2 = int(num_list[1])
s = 1
#
if max1 == max2:
	s = 0
elif max1 < max2:
	max1,max2 = max2,max1
#pick 2 numbers in the num_list random
for i in num_list:
	if i > max1:
		max2 = max1
		max1 = i
#if the picked number are same, go on 
	elif s == 0 and i < max1:
		max2 = i
		s = 1
	elif i > max2 and i < max1:
		max2 = i
print 'The biggest is %d , the second is %d ' % (max1,max2)