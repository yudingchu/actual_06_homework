a=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
b=a[:]
c=a[:]

print "The number are:",
for i in a:
  print i,

print

for l1 in a:
  for l2 in b:
    if l1 < l2:
      b.remove(l1);break

for l3 in b:
  print "The Max number:",l3
  c.remove(l3)


for l4 in a:
  for l5 in c:
    if l4 < l5:
      c.remove(l4);break

for l6 in c:
  print "The Second number:",l6

