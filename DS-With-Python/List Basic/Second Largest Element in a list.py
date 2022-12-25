def secondLargestElement(l):
	max = l[0]
	for x in l:
		if x>max:
			max = x
		else:
			pass
	# return max
	secMax = l[0]
	for x in l:
		if x>secMax and x!=max:
			secMax = x
	return secMax

l=[10,10,10]
print(secondLargestElement(l))