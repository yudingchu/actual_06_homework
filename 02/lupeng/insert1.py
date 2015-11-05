a = [-1,-2,4,3]
b = []
for i in range(len(a)):
    if len(b) == 0:
        b.append(a[i])
    else:
        for j in range(len(b)):
            if a[i] <= b[j]:
                b.insert(j,a[i])
                break
            elif j == len(b) - 1:
                b.insert(j+1,a[i])
                break
print b
