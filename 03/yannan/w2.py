# -*- encoding: utf-8 -*-
__author__ = 'yannan'
#作业：第二题统计字符数量之后，打印出现次数前10的字符
read_me = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
read_me1 = '''a bb ccc dddd eeeee ffffff gggg hhh ii j'''

#通过列表散列字符
list1 = list(read_me)
#通过空字典，统计字符个数
dict1 = {}
for i in list1:
    #如果字符重复，则key（字符）对应的value+1
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
#print dict1
#{'a': 1, ' ': 9, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 4, 'f': 6, 'i': 2, 'h': 3, 'j': 1}
list2 = []
#利用iteritems()将字典转成由元组构成的列表
for i in dict1.iteritems():
    list2.append(i)
#print list2
#由大至小，插入排序
m = 1
while m < len(list2):
    n = m
    list_top = list2[m]
    m += 1
    while n > 0 and list_top[1] > list2[n-1][1]:
        list2[n] = list2[n-1]
        n -= 1
    list2[n] = list_top
print list2
#print list2
#打印TOP10
top = 0
while top < 10:
    print list2[top]
    top += 1