
testlist = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,333,444,111,4,5,777,65555,45,33,45]
"""
a = max (testlist)
testlist.remove(a)
b = max(testlist)

print a,b
"""


test = 0
for max in testlist:
    if max > test:
        test2 = test
        test = max
        print test2,test,max
print test,test2 
    



