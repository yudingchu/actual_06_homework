#!/bin/env python
#Name: lizhen
#Date: 2015-10-27
#Homework for class 1 

name_list = [1,2,3,4,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_1=max_2=0

for i in name_list:
#when a is lower
    if max_1 < i:		
        max_2 = max_1		#the second max 
        max_1 = i 	#the first max
# when a is higher
    elif max_1 > i:
        if max_2 < i:
            max_2 = i  #the second max 
    else:
        pass      # the a equal i
print "The first max: ",max_1
print "The second max: ",max_2