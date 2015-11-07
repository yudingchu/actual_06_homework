data_list = []
while True:
    action = raw_input('please input add or show or exit:')
    if action == 'add':
        data = input('please input data:')
        if len(data_list) == 0:
            data_list.append(data)
        elif len(data_list) == 1:
           if data >= a[0]:
                data_list.append(data)
           elif data < data_list[0]:
                data_list.insert(0,data)
        elif len(data_list) != 0 and len(data_list) != 1:
            for num in range(len(data_list)):
                    if data > data_list[-1]:
                        data_list.append(data)
                        break
                    elif data > a[num]:
                        continue
                    elif data <= data_list[num]:
                        data_list.insert(num,data)
                        break
    elif action == 'show':
        print data_list
    elif action == 'exit':
        break
