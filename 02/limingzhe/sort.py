# -*- coding: utf-8 -*-

arr1 = [3,325,35,6,67,8,8,34,32,231,476,8,7,52,222,67,2,-1,324,0]
 
for j in range(1,len(arr1)):
    key = arr1[j]
    i = j-1
    #向前查找插入位置
    while i>=0 and arr1[i]>key:
        arr1[i+1] = arr1[i]
        i = i-1
    arr1[i+1] = key

print arr1