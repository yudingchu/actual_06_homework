#coding=utf-8
arr = [1,7,3,5,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,65555,45]
#对上面的list插入排序
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j-1]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
print arr
print len(arr)
