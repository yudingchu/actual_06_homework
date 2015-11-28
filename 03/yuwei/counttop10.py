#coding=utf-8
#作业：第二题统计字符数量之后，打印出现次数前10的字符(冒泡排序)
str1 = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

#通过list函数将字符转变成列表
list1 = list(str1)
#通过空字典，统计字符数
dicts = {}

#统计字符串出现的次数
for i in list1:
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1
#print dicts


nums = []
list2 = []
#通过冒泡排序取出最大的10个值,从小到大冒泡
nums = dicts.values()
for i in xrange(len(nums)):
    for j in xrange(len(nums)-1-i):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
#print nums[len(nums)-10:]

#判断字典dicts的value是否在nums里，如果在就将key和value以tuple的形式添加到list2中
for k in dicts:
    if dicts[k] in nums[len(nums)-10:]:
        tuple1 = (k,dicts[k])
        list2.append(tuple1)
print list2
