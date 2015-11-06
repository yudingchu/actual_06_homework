a_list = [2,4,533,2,3]
b_list = [34,44,32,22,2,3,5,533,4]
result_list = []

for temp in a_list:
    if temp in b_list:
        if temp not in result_list:
            result_list.append(temp)

print (result_list)
        
    
