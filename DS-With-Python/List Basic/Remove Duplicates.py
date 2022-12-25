def removeDups(arr):
	n = len(arr) -1
	newl=[]
	for i in arr:
		newl.append(i)
	for x in range(n):
		if arr[x] == arr[x+1]:
			newl.remove(arr[x])
	return newl

arr = [10,20,20,30,30,30,30,50]
print(removeDups(arr))