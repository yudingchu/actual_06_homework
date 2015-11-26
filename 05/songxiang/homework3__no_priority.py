#  -*- coding:utf-8 -*-
def caculate(symbol,number):
	if len(symbol) != len(number)-1:
		return "error, 运算符和数字数量不匹配 please re-input "
	for i in symbol:
		if i == '+':
			result = float(number[0])+float(number[1])
			number[:2] = [result]
		elif i == '-':
			result = float(number[0])-float(number[1])
			number[:2] = [result]
		elif i == '*':
			result = float(number[0])*float(number[1])
			number[:2] = [result]
		elif i == '/' and number[1] != '0':
			result = float(number[0])/float(number[1])
			number[:2] = [result] 
		else :
			return "error, O can't be divided "
	return number[0]
def operate(string):
	string.strip()
	symbol = []
	string_new = ''
	numbers = ['1','2','3','4','5','6','7','8','9','0',' ']
	if string[0] not in numbers:
		return 'error, 符号再数字前面' 
	for i in string:
		if i == '+' or i == '-' or i == '*' or i == '/':
			symbol.append(i)
			string_new = string_new + ','
		elif i in numbers:
			string_new = string_new + i
		else:
			return 'error,包含非法字符 pleses re-input '
	number = string_new.split(',')
	result = caculate(symbol, number)
	return result
if __name__ == '__main__':
	a = '+1+ 20 +0+65+98'
	result = operate(a)
	print result
	