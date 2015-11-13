# -*- encoding: utf-8 -*-
__author__ = 'yn'

#用插入算法排序list
arr2 = [-1,2567,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
__author__ = 'ynzilla'
arr1 = [3,325,35,6,67,8,8,34,32,231,476,8,7,52,222,67,2,-1,324,0]
i=1
while i < len(arr1):
    j=i
    arr=arr1[i]
    i=i+1
    while j > 0 and arr > arr1[j-1]:
        arr1[j]=arr1[j-1]
        j=j-1
    arr1[j]=arr
    #print arr1