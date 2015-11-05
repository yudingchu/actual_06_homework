#/usr/bin/env python
arr = []

while True:
	user_input = raw_input('please insert your number: ').strip()
	if len(user_input) == 0:
		print "it can not be empty!!!"
		continue
		
	num = int(user_input)
	arr.append(num)
	if len(arr) == 0:
		arr.append(num)
		print arr
		continue
	else:
		for i in range(1,len(arr)):
			key = arr[i]
			j = i
			while j > 0 and arr[j-1] > key:
				arr[j] = arr[j-1]
				arr[j-1] = key
				j -= 1

	print arr