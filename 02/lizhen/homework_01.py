arr_1_list = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr_2_list = [2,1,3,2,43,234,454,452,234,14,21,14]
same_list=[]

for num1 in arr_1_list:
        if num1 in arr_2_list and num1 not in same_list:
            same_list.append(num1)
print same_list