try:
    f = open('www_access_20140823.log')
except IOError:
    print 'file not exist!'
else:
    lines = f.readlines()
    temp = []
    count = {}
    top_10 = []
    for line in lines:
        temp = line.split(' ')
        key = tuple([temp[8],temp[6],temp[0]])
        count[key] = count.setdefault(key,0) + 1
    for key in count:
        top_10.append([count[key],key])
    top_10.sort()
    top_10.reverse()
    for num in range(10,len(top_10)):
        if top_10[num][0] == top_10[9][0]:
            continue
        elif top_10[num][0] != top_10[9][0]:
            top_10 = top_10[:num]
            break
    print top_10
    print len(top_10)
