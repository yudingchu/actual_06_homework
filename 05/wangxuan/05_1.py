#!/usr/bin/env python


d = {'a':1,'b':2,'c':3}
print sorted(d.iteritems(),key = lambda k:k[1],reverse = True)
print sorted(zip(d.values(),d.keys()),reverse = True)

