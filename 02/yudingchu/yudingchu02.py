arr=[1100,1100,1110,10,1,234,2,5,1,66,100000,23,11,6,112,100,120,112,1300,1109,110,1100,-9,114,119]
#arr=[11,1,234,2,5,1,55]
arr1=[]
j=0
for i in arr:
    if len(arr1)==0:
        arr1.append(i)
        continue
    for j in range(len(arr1)):
        if i<=arr1[j]:
            arr1.insert(j,i)
            break
        elif j==len(arr1)-1:
            arr1.append(i)
            break
print arr1
