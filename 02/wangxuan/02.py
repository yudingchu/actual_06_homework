a = [2,1,4,3,6,0]
b = a[0:1]
for i in range(1,len(a)):
	for j in range(len(b)):
		if a[i] >= b[j]:
			b.insert(j,a[i]) 
			break
		elif a[i] < b[j] and j == len(b)-1:
			b.append(a[i])
			break
			
print b 
