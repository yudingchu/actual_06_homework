ngxfile = open('www_access_20140823.log')
logs_list = ngxfile.readlines()
ngxfile.close()
count_dict = {}
result_list = []
for log_list in logs_list:
    line_list = log_list.split(' ')
    field_tuple = (line_list[8],line_list[6],line_list[0])
    if field_tuple in count_dict:
        count_dict[field_tuple] += 1
    else:
        count_dict[field_tuple] = 1
for temp in count_dict:
    result_list.append(temp[0])
    result_list.append(temp[1])
    result_list.append((temp[2],count_dict[temp]))
    print(result_list)
    result_list.clear()


    
    
    
