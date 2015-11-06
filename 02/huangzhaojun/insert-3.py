num_list = []
alphabet_list = []
while True:
        action = raw_input('please input add or print or exit:')
        if action == 'add':
                data = raw_input('please input num or alphabet:')
                if data == 'num':
                        num = input('please input num:')
                        num_list.append(num)
                        num_list.sort()
                elif data == 'alphabet':
                        alphabet = raw_input('print input alphabet:')
                        alphabet_list.append(alphabet)
                        alphabet_list.sort()
        elif action == 'print':
                show = raw_input('please input num or alphabet:')
                if show == 'num':
                        print num_list
                elif show == 'alphabet':
                        print alphabet_list
        elif action == 'exit':
                break
        else:
                print 'input add or print or exit!'
