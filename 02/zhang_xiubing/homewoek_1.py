a=[1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12, 3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]
b=[2, 1, 3, 2, 43, 234, 454, 452, 234, 14, 21, 14]

new_list=[]
for i in a:
	if i in b and i not in new_list:
		new_list.append(i)
print new_list
