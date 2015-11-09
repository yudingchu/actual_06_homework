read_me = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
number=[]
words=[]
for i in read_me:
	if i not in words:
		words.append(i)
		number.append(1)
	else:
		number[words.index(i)] = number[words.index(i)]+1		
for i in range(len(number)-2):
	for j in range(len(number)-i-2,-1,-1):
		if number[j] < number[j+1]:
			number[j],number[j+1]=number[j+1],number[j]
			words[j],words[j+1]=words[j+1],words[j]
print number
for i in range(10):
	print 'the %d is word %s , and is %d words ' % (i+1,words[i],number[i])