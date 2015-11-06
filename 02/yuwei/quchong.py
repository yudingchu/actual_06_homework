#coding=utf-8
num_list= [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#对上面的list去重
unqiue_list = []
for i in num_list:
    if i not in unqiue_list:
        unqiue_list.append(i)
print unqiue_list
