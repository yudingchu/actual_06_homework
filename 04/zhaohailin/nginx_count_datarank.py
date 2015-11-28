#!/usr/bin/env python
# -*- coding: utf-8 -*-

#处理nginx的log，以用户，访问链接，访问httpd状态三个维护来进行数据同步，打印出访问量前十的用户IP
#IP
#"GET /data/uploads/2013/0322/10/514bc44910ed6.jpg HTTP/1.1"
#200
#期望输出一个list，分别存储这http状态，访问url，ip，访问次数

logs = open("c:/www_access_20140823.log")

contents = logs.readlines()
logs.close()

new_dict = {}

for lines in contents:
    ip = lines.split()[0]
    url = lines.split()[6]
    http_code = lines.split()[8]
    tuple_list = (ip,url,http_code)

    if tuple_list in new_dict:
        new_dict[tuple_list] = new_dict[tuple_list] + 1  # new_dict[tuple_list] += 1
    else:
        new_dict[tuple_list] = 1
    # print new_dict[tuple_list]

for show_list in sorted(new_dict.items(),key=lambda arr:arr[1])[:-10:-1]:  #参考网上key=lambda
    print show_list