name_list = [1,2,3,45,6]
a=b=0
for i in name_list:
  if a < i:
      b = a
	  a = i 
  elif a > i:
      if b < i:
	      b = i 
  else:
       pass 
print "The first max: ",a
print "The second max: ",b