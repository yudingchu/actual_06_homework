#!/usr/bin/env python

nums = [77,1,2,3,4,2,-12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4,-882]
for i in xrange(len(nums)):
	value = nums[i]
	j = i - 1
	while j >= 0:		
		if nums[j] > value:
			nums[j+1] = nums[j]
			nums[j] = value
		j -= 1
print nums