num_list = [1111111111111,23,42,85,45,1,1,4,-1,-10,4,5454,68,54545,6464575,43,999999999]
new_list = []
for num in num_list:
    if len(new_list) == 0:
        new_list.append(num)
        continue
    for i in range(len(new_list)):
        if new_list[i] > num:
            new_list.insert(i,num)
            break
    else:
         new_list.append(num)  
         # new_list.insert(i+1,num)
print new_list