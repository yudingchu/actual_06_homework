# -*- coding: utf-8 -*-
'''
•一个list[(1,4),(5,1),(2,3)],根据每个元组中的较大值进行排序 ◦期待结果：[(2,3),(1,4),(5,1)]
◦要求：用sorted和lambda完成
◦级别1：用lambda中用max
◦级别2：lambda中不用max
◦提示：True乘以4 ==4 Fale乘以2 == 0
'''

sort_list = [(1,4),(5,1),(2,3)]
print(sorted(sort_list,key = lambda x: max(x)))
