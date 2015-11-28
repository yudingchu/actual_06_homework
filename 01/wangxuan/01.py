a = [1,2,3,2,4,5]
b = a[0:2]
if b[0]<b[1]:
	b[0],b[1] = b[1],b[0]
	
for i in xrange(2,len(a)):
	if a[i] > b[0]:
		b[0],b[1] = a[i],b[0]
		continue 
	elif a[i] > b[1]:
		b[1] = a[i]
print b 
