arr1 = [1,21,2,2,3,3550,567,4,5,4325,1200,33,80]
arr2 = []
for i in arr1:
    if len(arr2) == 0 or i > arr2[len(arr2)-1]:
        arr2.append(i)
    else:
        for n in range(len(arr2)):
            if i <= arr2[n]:
                arr2.insert(n,i)
                break
print arr2