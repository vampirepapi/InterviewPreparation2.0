def getEleAtIdx(n, l, idx):
    if n - 1 < idx:
        return -1
    for i in range(0, n):
        if i == idx:
            return l[i]


n = 4
arr = [1, 2, 3, 4]
index = 0
print(getEleAtIdx(n, arr, index))
