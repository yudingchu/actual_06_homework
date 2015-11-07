arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
zone_list = []
for j in arr1: 
    if j in arr2 and j not in zone_list:
        zone_list.append(j)
print zone_list
            
