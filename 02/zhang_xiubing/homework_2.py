a_list=[1,2,3,2,12,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

for i in range(1,len(a_list)):
	tmp=a_list[i]
	j=i
	while j>0 and a_list[j-1]>tmp:
		a_list[j]=a_list[j-1]
		j=j-1
	a_list[j]=tmp
print a_list
