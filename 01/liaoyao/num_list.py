#/usr/bin/env python
nums = [1,2,3,2,12223,7690,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max1 = 0
max2 = 0
for i in nums:
        if i > max1:
                max2 = max1
                max1 = i

print 'The firsr number is: %s' % max1
print 'The second number is: %s' % max2