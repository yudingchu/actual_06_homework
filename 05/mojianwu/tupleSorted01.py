#coding:utf-8

# 一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序
# 期待结果：[(2,3),(1,4),(5,1)]
# 要求：用sorted和lambda完成
# 级别1：用lambda中用max
# 级别2：lambda中不用max
# 提示：True乘以4 ==4 False乘以2 == 0
# 	print True*4
# 	print False*2
# list = [(1,4),(5,1),(2,3)]
list = [(1,4),(5,1),(2,3),(3,2),(6,1)]
list_sorted1 = sorted(list, cmp=lambda x,y:cmp(max(x[0],x[1]),max(y[0],y[1])))
print list_sorted1

list_sorted2 = sorted(list, key=lambda x:max(x))
print list_sorted2

list_sorted3 = sorted(list, key=lambda x:x[0] if x[0] > x[1] else x[1])
print list_sorted3