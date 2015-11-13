data_list = []
num_list= []
while True:
    action = raw_input('add or exit:')
    if action == 'add':
        data = input('input data:')
        if len(data_list) == 0:
            data_list.append(data)
            print data_list
        elif len(data_list) == 1:
           if data > data_list[0]:
                data_list.append(data)
                print data_list
           elif data <= data_list[0]:
                data_list.insert(0,data)
                print data_list
        elif len(data_list) != 0 and len(data_list) != 1:
            num_list = range(len(data_list))
            num_list.reverse()
            for num in num_list:
                    if data >= data_list[num]:
                        data_list.insert(num+1,data)
                        print data_list
                        break
                    elif data < data_list[num]:
                        print data_list
                        continue
    elif action == 'exit':
        break
