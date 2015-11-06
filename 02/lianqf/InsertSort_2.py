sort_list = [1,2,5,18,3,55,233,13,3333]
for i in range(1,len(sort_list)):
    j = i
    temp = sort_list[i]
    while j > 0 and temp > sort_list[j - 1]:
        sort_list[j] = sort_list[j - 1]
        j-=1
    sort_list[j] = temp

print (sort_list)
