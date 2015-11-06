data_list=[]
while True:
    action = raw_input('please input add or show or exit:')
    if action == 'add':
        data = input('please input data:')
        data_list.append(data)
        for num in range(len(data_list)):
            if data > data_list[num]:
                continue
            elif data <= data_list[num]:
                data_list.insert(num,data_list.pop())
                break
    elif action == 'show':
        print data_list
    elif action == 'exit':
        break
