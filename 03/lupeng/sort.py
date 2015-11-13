__author__ = 'lupeng'
read_me = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
read_me1 = '''a bb ccc dddd eeeee ffffff gggg hhh ii j'''
str1 = str(read_me)
dict1 = {}
for i in str1:
    if i in dict1:
        dict1[i] = dict1[i]+1
    else:
        dict1[i] = 1
str2 = []

for i in dict1.iteritems():
    str2.append(i)
for a in range(len(str2)-1):
        for b in range(len(str2)-1-a):
            if str2[b+1][1] > str2[b][1]:
                str2[b],str2[b+1] = str2[b+1],str2[b]
arr = 0 
while arr < 10:
    print str2[arr]
    arr = arr+ 1
