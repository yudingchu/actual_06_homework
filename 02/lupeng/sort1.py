arr = [1,2,3,123,11,123,421,124,2,3,4,5,6]
for j in range(len(arr)-1):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
print arr
