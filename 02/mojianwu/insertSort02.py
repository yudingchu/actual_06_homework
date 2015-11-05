#/usr/bin/env python
arr = []

while True:
	user_input = raw_input('please insert your number: ').strip()

	if user_input == 'quit':
		exit('exit!!!')

	if len(user_input) == 0:
		print "it can not be empty!!!"
		continue
		
	num = int(user_input)
	arr.append(num)
	for i in range(1,len(arr)):
		key = arr[i]
		while i > 0 and arr[i-1] > key:
			arr[i] = arr[i-1]
			arr[i-1] = key
			i -= 1

	print arr