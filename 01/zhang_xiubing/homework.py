d=[1,2,3,2,12,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
m=1
for i in d:
	if m>i:
		pass
	else:
		m=i
print m

n=m
for j in d:
	c=m-j
	if 0<c<n:
		b=j
		n=c
	else:
		a=1
		if b>1:
			a=b
		else:
			pass
print a
					
