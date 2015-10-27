#!/bin/env python
#Name: lizhen
#Date: 2015-10-27
#Homework for class 1 

name_list = [1,2,3,4,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
a=b=0

for i in name_list:
#when a is lower
  if a < i:		
      b = a		#the second max 
	  a = i 	#the first max
# when a is higher
  elif a > i:
      if b < i:
	      b = i  #the second max 
  else:
       pass      # the a equal i
print "The first max: ",a
print "The second max: ",b