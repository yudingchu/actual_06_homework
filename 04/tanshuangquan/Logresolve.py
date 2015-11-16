logfile=open("www_access_20140823.log","r")
loglist=logfile.readlines()
logfile.close()
logdict={}
loglist2=[]

for logline in loglist:
    linelist=logline.split()
    j=linelist[8], linelist[6], linelist[0]
   # print j
    if j not in logdict:
        logdict[j] = 1
    else:
        logdict[j] += 1

for logitem ,num in logdict.iteritems():
    
    l1=list(logitem)
    l=l1[:2]
    l.append((l1[2],num))
    loglist2.append(l)


for logi in range(len(loglist2)-1):
    for logj in range(len(loglist2)-1-logi):
        if loglist2[logj][2][1] > loglist2[logj+1][2][1]:
            loglist2[logj],loglist2[logj+1] = loglist2[logj+1],loglist2[logj]


for i in loglist2[:-11:-1]:
    print i
    

