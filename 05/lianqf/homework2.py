# -*- coding: utf-8 -*-
'''
•实现加减乘除功能的函数 ◦级别1 不支持优先级
◦级别2 支持优先级，但是没有括号
◦def operate(str): ◾pass

◦不支持优先级情况
◦operate('1+2+3-5') == 1
◦operate('10+2*3-5') == 31
◦operate('-1+2+3-5') == -1
'没考虑负数和（），考虑优先级
'''



def Str2List (str_equation):
    Sign = ('+','-','*','/')
    temp = ''
    list_equation = []
    for i in str_equation:
        if i in Sign :
            list_equation.append(int(temp))
            temp = ''
            list_equation.append(i)
        else:
            temp += i
    list_equation.append(int(temp))
    return list_equation


def Counting(Sign,list_operation):
    list_temp = list_operation[:]
    while Sign in list_temp:
        sign_idx = list_temp.index(Sign)
        if Sign == '*':
            result_num = list_temp[sign_idx - 1] * list_temp[sign_idx + 1]
        if Sign == '/':
            result_num = list_temp[sign_idx - 1] / list_temp[sign_idx + 1]
        if Sign == '+':
            result_num = list_temp[sign_idx - 1] + list_temp[sign_idx + 1]
        if Sign == '-':
            result_num = list_temp[sign_idx - 1] - list_temp[sign_idx + 1]    
        list_temp.pop(sign_idx - 1)
        list_temp.pop(sign_idx - 1)
        list_temp.pop(sign_idx - 1)
        list_temp[sign_idx - 1:sign_idx - 1] = [result_num ]
    return list_temp


def int_Computed(list_opt):
    list_counting = list_opt[:]
    while len(list_counting) > 1:
        list_counting = Counting('*',list_counting)
        list_counting = Counting('/',list_counting)
        list_counting = Counting('+',list_counting)
        list_counting = Counting('-',list_counting)
    int_result = list_counting[0]
    return int_result

list_S2L = Str2List('-1+2+3-5')
int_computed = int_Computed(list_S2L)
print int_computed




    
    
