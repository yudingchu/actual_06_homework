def kuaisupaixu(num_list,left,right):
	i = left
	j = right
	if i == j:
		return num_list
	while j > i:
		while j > i and num_list[j] >= key:
			j = j - 1
		num_list[i],num_list[j] = num_list[j],num_list[i]		
		while i < j and num_list[i] <= key:
			i = i + 1	
		num_list[i],num_list[j] = num_list[j],num_list[i]
	return num_list.index(key)
	kuaisupaixu(num_list,num_list.index(key),i)
	kuaisupaixu(num_list,j,num_list.index(key))
	return num_list
if __name__ == '__main__':
	num_list = [9999,99999,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,33,45]
	key = num_list[0]
	right = len(num_list)-1
	left = 0
	kuaisupaixu(num_list,left,right)
	print num_list