nums = [55,779999,2,8987563,7690,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45，88885555,55475]
a=b=0
for s in nums:
        if a < s:
               b = a
               a = s
        elif a > s:
             if b < s:
                b = s
print 'The first number is: %s' % a
print 'The second number is: %s' % b
