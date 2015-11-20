f = open('www_access_20140823.log','r')
f_list = f.readlines()
f.close()
d = {}
finalfile = open('copy.log','a+')
final_list= ''
count = 0
for i in f_list:
        new = ['']*3
        one_list = i.split(' ')
        new[0] = one_list[8]
        new[1] = one_list[6]
        if one_list[0] in d:
                d[one_list[0]] = d[one_list[0]] + 1
        else:
                d[one_list[0]] = 1
        new[2] = (one_list[0],d[one_list[0]])
        #print new[2]
        finalstr = str(new)
        final_list = final_list+ finalstr + '\n'
finalfile.writelines(final_list)
finalfile.close()
