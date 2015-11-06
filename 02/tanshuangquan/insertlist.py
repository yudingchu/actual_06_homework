num_list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
if len(num_list) == 1:
    print num_list
    exit()

for i in range(1,len(num_list)):
    temp=num_list[i]
    j = i - 1
    while j >= 0 and temp < num_list[j]:
        num_list[j+1] = num_list[j]
        j -= 1
    num_list[j+1] = temp

print num_list
    
