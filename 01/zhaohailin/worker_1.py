list=[1,7,3,5,12,3,1,3,21,2,2,3,4111,22,8888,444,111,4,5,777,66666,45,33,45]

num1 = 0
num2 = 0

for i in list:
    if i > num1:
        num1 = i
for i in list:
    if i > num2 and i < num1:
        num2 = i

print 'max1 is %s'  %(num1)
print 'max2 is %s'  %(num2)