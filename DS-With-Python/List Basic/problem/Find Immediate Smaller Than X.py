def immediateSmaller(arr,n,x):
    res = -1
    for i in arr:
        if x>i and i>res:
            res = i

    return res

n = 5
arr = [16,67,12,15,13]
x = 16

print(immediateSmaller(arr, n, x))
