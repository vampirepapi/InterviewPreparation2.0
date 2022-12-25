def revList(l):
	newL = []
	n = len(l)-1
	
	while n>=0:
		newL.append(l[n])
		n=n-1

	return newL


l = [10,20,20,30]
l = ['Shubham', 'Sourabh', 'Gupta']
print(revList(l))

# using library methods
print(l.reverse())
print(l[::-1])