#-*- coding:utf-8 -*-
def kuaisupaixu(num_list,left,right):
	i = left
	j = right
	key = num_list[left]
	if i == j:
		return num_list
	while j > i:
		while j > i and num_list[j] >= key:
			j = j - 1
		num_list[i],num_list[j] = num_list[j],num_list[i]		
		while i < j and num_list[i] <= key:
			i = i + 1	
		num_list[i],num_list[j] = num_list[j],num_list[i]
	kuaisupaixu(num_list,i+1,right)
	kuaisupaixu(num_list,left,j)
if __name__ == '__main__':
	num_list = [2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,45,33,45]
	'''
	99999,99999,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45
	就不可以
	'''
	kuaisupaixu(num_list,0,len(num_list)-1)
	print num_list