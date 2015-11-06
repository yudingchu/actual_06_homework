list1=[1,7,3,5,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max1=max2=0
for i in list1:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i
print "the first big number is %s" %(max1)
print "the second big number is %s" %(max2)
