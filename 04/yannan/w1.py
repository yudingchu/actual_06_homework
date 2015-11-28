# -*- encoding: utf-8 -*-
__author__ = 'yannan'

'''
小练习
简单的nginx日志分析

    日志文件在/home/shre/www_access_20140823.log
    期望输出一个list，分别存储这http状态，访问url，ip，访问次数，如下图

'''
#f = open('D:\\yncode\\20151114\\home\\test')
t2=[]
d1={}
f = open('www_access_20140823.log')
#f = open('test')
t1 = f.read().split('"-"\n')
f.close()
for i in xrange(len(t1)-1):
    tmp1 = t1[i].split(' ')[8],t1[i].split(' ')[6],t1[i].split(' ')[0]
    t2.append(tmp1)
    if t2[i] in d1:
        d1[t2[i]] += 1
    else:
        d1[t2[i]] = 1
'''
for j in t2:
    if j in d1:
        d1[j] += 1
    else:
        d1[j] = 1
'''
t3=d1.items()
t4=[]
for k in xrange(len(t3)-1):
    for l in xrange(len(t3)-1-k):
        if t3[l+1][1]>t3[l][1]:
            t3[l+1],t3[l]=t3[l],t3[l+1]
for o in t3:
    tmp2=o[0][2],o[1]
    tmp3=o[0][0],o[0][1],tmp2
    print list(tmp3)


