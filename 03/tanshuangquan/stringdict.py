str1 = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''

s_dict={}

for i in str1:
    i=i.strip()
    if i == '':
        continue
    if i not in s_dict:
        s_dict[i]=1
    else:
        s_dict[i] += 1

#for j,k in s_dict.items():
#    print j,k
print s_dict
s_keys=s_dict.keys()
s_values=s_dict.values()
s_values2=s_dict.values()
print s_values

for k in (range(len(s_values)-1)):
    for j in (range(len(s_values)-1)):
        if s_values[j]>s_values[j+1]:
            s_values[j],s_values[j+1] = s_values[j+1],s_values[j]

print s_values
jsq=0
cs_v=s_values[-1:-11:-1]
print cs_v
for topten in cs_v:
    if jsq > 1:
       jsq -= 1
       continue
    
    if s_values2.count(topten) == 1:
        s_index=s_values2.index(topten) 
        print "Top",cs_v.index(topten),":",s_keys[s_index]
    else:
        jsq=s_values2.count(topten)
        s_index=0
        for i in range(jsq):
            if i ==0:
                s_index=s_values2.index(topten,s_index)
            else:
                s_index=s_values2.index(topten,s_index+1)
            print "Top",cs_v.index(topten),":",s_keys[s_index]


