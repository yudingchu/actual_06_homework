#!/bin/env python
#coding:utf-8

#解析用户输入的字符串成列表
def gener_list(str_input,opt_str=['+','-','*','/']):
    new_list = []
    num_str = ''
    for i in str_input:
        if i.isdigit() or i == '.':
            num_str += i 
            continue
        if i in opt_str:
            new_list.extend([num_str,i])
            num_str=''
            continue
        raise IOError
    new_list.append(num_str)
    return new_list

#计算表达式
def opt(num_oprand,num_opt,opration='+'):
    num_oprand,num_opt = float(num_oprand),float(num_opt)
    opt_dict = { '+' : num_oprand + num_opt,
                 '-' : num_oprand - num_opt,
                 '*' : num_oprand * num_opt,
                 '/' : num_oprand / num_opt 
               }
    if opration == '/' and num_opt == 0:
        raise ZeroDivisionError
    return opt_dict.get(opration)

#计算用户输入
def rec(rec_list,prio=['*','/']):
    while True:
        for i in range(len(rec_list)):
            if rec_list[i] in prio:
                s,opration,n = rec_list[i-1],rec_list[i],rec_list[i+1]
                s = opt(s,n,opration)
                rec_list[i-1:i+2] = [s]
                print rec_list
                return rec(rec_list,prio)
        else:
           if len(rec_list) == 1:
               return rec_list[0]
           return rec(rec_list,prio=['+','-','*','/'])

if __name__ == "__main__":
	str_input = '1+2.1/3+5-4*4'
	new_list = gener_list(str_input)
	#pririoty_list指定优先级,默认先算乘除,后算加减
	'''
	#无优先级
	pririoty_list = ['+','-','*','/']  
	value = rec(new_list,pririoty_list)
	'''
	#优先级
	value = rec(new_list)
        print value
	
