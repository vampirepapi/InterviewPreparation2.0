def deleteFromArr(arr, n, idx):
    arr = [x for x in range(1, n+1)]
    for i in range(n):
        if i == idx:
            arr.remove(arr[i])
            arr.append(0)
    return arr


n = 5
arr = [i+1 for i in range(n)]
idx = 0
print(deleteFromArr(arr, n, idx))
