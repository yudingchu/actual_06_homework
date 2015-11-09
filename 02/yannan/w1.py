# -*- encoding: utf-8 -*-
__author__ = 'yn'

#求两个数组都有的元素，并且去重
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
arr3 = []

for i in arr2:
    if i in arr1 and i not in arr3:
        arr3.append(i)
print arr3