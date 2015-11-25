#!/usr/bin/env python

#NBL
from collections import deque
import pdb

cal_op = ('+','-','*','/','(',')')
cal_op_less=('+','-','*','/')
#'1+20-(2+3)'---->['1','+','20','-','(','2','+','3',')']
def my_split(input_str):
	tmp = ''
	lst = []
	for i in input_str:
        	while (i not in cal_op):
                	tmp += i
                	break
        	if i in cal_op:
                	if tmp != '':
                        	lst.append(tmp)
                	lst.append(i)
                	tmp = ''
	if tmp != '':
		lst.append(tmp)
	return lst

def nbl(lst_cont):
	s1 = ['#']
	s2 = []
	dq_lst = deque(lst_cont)
	for i in xrange(len(lst_cont)):
		process_x = dq_lst.popleft()
		if process_x not in cal_op:
			s2.append(process_x)
		if process_x == '(':
			s1.append(process_x)
		if process_x == ')':
			while s1[-1] != '(':
				s2.append(s1.pop())
			s1.pop()
		if process_x in cal_op_less:
			if s1[-1] == '(':
				s1.append(process_x)
			elif process_x == '*' or process_x == '/':
				if s1[-1] == '+' or s1[-1] == '-' or s1[-1] == '#':					
					s1.append(process_x)
				else:
					while (s1[-1] != '(' and s1[-1] != '+' and s1[-1] != '-' and s1[-1] != '#'):
						s2.append(s1.pop())
					s1.append(process_x)
			elif process_x == '+' or process_x == '-':
				while (s1[-1] != '(' and s1[-1] != '#'):
					s2.append(s1.pop())
				s1.append(process_x)
#		pdb.set_trace()				
	while len(s1) > 1:
		s2.append(s1.pop())				
	return s2


def count_op(s2):
	cal = []
	dq_s2 = deque(s2)
	for i in xrange(len(s2)):		
		op = dq_s2.popleft()
		if op not in cal_op_less:
			cal.append(op)
		if op in cal_op_less:
			cal1 = float(cal.pop())
			cal2 = float(cal.pop())
			if op == '+':
				result = cal1 + cal2
				cal.append(result)
			if op == '-':
				result = cal2 -cal1
				cal.append(result)
			if op == '*':
				result = cal1 * cal2
				cal.append(result)
			if op == '/':
				result = cal2 / cal1
				cal.append(result)
	return cal	

while True:
	input_str = raw_input('INPUT:')
	if input_str == 'exit':
		break
	else:
		lst_cont = my_split(input_str)
		s2 = nbl(lst_cont)
		print count_op(s2)
