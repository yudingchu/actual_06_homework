#!/bin/env python
#-*- coding:utf8 -*-

#log_file = '10_access.log'
#log_file = 'www_access.log'
log_file = 'www_access_20140823.log'
log_dict = {}
log_count_dict = {}
with open(log_file) as f:
    for line in f.xreadlines():
        #print line
        ip  = line.split()[0]
        url = line.split()[6]
        code= line.split()[8]
        #print ip,url,code
        if  not log_dict.has_key(ip):
           log_dict.update({ip:{url:{code:1}}})
        else:
           if not log_dict[ip].has_key(url):
               log_dict[ip].update({url:{code:1}})
           else:
           
               log_dict[ip][url].update({code:log_dict[ip][url].get(code,0) + 1})

#print log_dict
#for ip_count in log_dict:
    #print ip_count
for ip in log_dict:
  for url in log_dict.get(ip):
    for code in log_dict[ip][url]:
        log_count_dict.update({ (ip,url,code): log_dict[ip][url].get(code) })
    #ip_count =  sum(log_dict[ip].get(url).values())
    #log_count_dict.update({ip:ip_count})
    #log_count_dict.update({ (ip,url,)  })
count_list = []
'''
for v in log_count_dict.iteritems():
    #print v[1],v[0]
    count_list.append((v[1],v[0]))
    count_list.sort()
print count_list[:-10:-1]
'''
'''
for key in log_count_dict:
  if len(count_list) == 0:
    count_list.append((key,log_count_dict[key]))
  for i in range(len(count_list)):
    if log_count_dict[key] <  count_list[i][1]:
      count_list.insert(i,(key,log_count_dict[key]))
      break
  else:
    count_list.append((key,log_count_dict[key]))
#print count_list[:-10:-1]
'''
#print log_count_dict
count = 10
if count > len(log_count_dict):
  count = len(log_count_dict)
for i in range(count):
  max_value = 0
  for key in log_count_dict:
    if max_value > log_count_dict[key]:
      continue
    else:
      max_value = log_count_dict[key]
      max_key = key
  else:
    #print max_key
    max_value = log_count_dict.pop(max_key)
    count_list.append((max_key,max_value))
with open('log_ansis.log','w') as f:
  for i in count_list:
    write_lines = i[0][0] +' ' +  i[0][1] +' '+ i[0][2] +' '+ str(i[1]) + '\n'
    f.write(write_lines)
     
