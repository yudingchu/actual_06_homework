char_str = "first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!"
#char_str = "first of all, i want make it"
list_str = list(char_str)
dict_str = {}

#字符串转换数组
for temp in list_str:
    if temp in dict_str:
        dict_str[temp] = dict_str[temp] + 1
    else:
        dict_str[temp] = 1
print (dict_str)

list_num = list(dict_str.values())
print (list_num)

#冒泡排序次数top10
values_count = len(list_num)
for i in range(1,11):
    for j in range(1,values_count):
        if list_num[j - 1] > list_num[j] :
            list_num[j - 1],list_num[j] = list_num[j],list_num[j-1]
print (list_num)

#打印结果
result_dict = {}
temp_up = ''
for i in range(1,11):
    temp = list_num[len(list_num) - i]
    for top_char in dict_str:
        if dict_str[top_char] == temp:
            if temp != temp_up:
                print ('char is %s ,number is %d'  %(top_char,temp))
    temp_up = temp    
