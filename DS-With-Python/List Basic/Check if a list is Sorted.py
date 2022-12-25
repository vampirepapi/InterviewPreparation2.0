def sortedList(l):
	flag = True
	if len(l) == 1 or len(l) == 0:
		return flag
	n = len(l)
	for x in range(0,n-1):
		if l[x] > l[x+1]:
			flag = False
			break
		else:
			flag = True

	return flag

def isSorted(l):
	sl = sorted(l)

	if l==sl:
		return True
	else:
		return False

l = [10,20,20,30]
print(isSorted(l))
print(sortedList(l))



