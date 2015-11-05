def kuaisupaixu(num_list,i,j):
	if i == j:
		return num_list
	while j > i:
		while j > i :
			if num_list[j] < key:
				num_list[i],num_list[j] = num_list[j],num_list[i]
			j = j - 1
			break		
		while i < j:
			if num_list[i] > key :
				num_list[i],num_list[j] = num_list[j],num_list[i]
			i = i + 1
			break
	kuaisupaixu(num_list,0,i-1)
	kuaisupaixu(num_list,j+1,lengh)
	return num_list
if __name__ == '__main__':
	num_list = [99999,99999,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
	key = num_list[0]
	lengh = len(num_list)-1
	i = 0
	j = lengh
	kuaisupaixu(num_list,i,j)
	print num_list