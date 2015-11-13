read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
list_count=list(read_me)
dict_count={}
for key in list_count:
    if key in dict_count:
        dict_count[key]=dict_count[key]+1
    else:
        dict_count[key]=1
#print dict_count
tmp_dict={}
for key in dict_count:
    tmp_dict[dict_count[key]]=key
#print tmp_dict
key_list=list(tmp_dict.keys())
sort_key_list=sorted(key_list)
sort_10_list=sort_key_list[-1:-11:-1]
list_10=[]
for i in sort_10_list:
    list_10.append(tmp_dict[i])
print list_10


#tmp_dict1=list(tmp_dict)
#print key_list
#print sort_list
#print sort_10_list
