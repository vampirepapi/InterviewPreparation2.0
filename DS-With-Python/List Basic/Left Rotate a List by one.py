def rotateArr(l):
    n = len(l)
    x = l[0]

    for i in range(1,n):
        l[i-1] = l[i]
    
    l[n-1] = x
    return l

arr = [10,20,20,30,30,30,30,50]
print(rotateArr(arr))

neew = [1,2,3,45]


prnt(new)

