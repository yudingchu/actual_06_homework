arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
result = []
for num in range(len(arr1) - 1):
	if arr1[num] in arr2 and arr1[num] not in result:
		result.append(arr1[num])
		sorted(result)
print result
