def immediateGreater(arr,n,x):
    
        num = 10000
        ans = -1 
        
        for i in arr:
            if i > x:
                if i < num:
                    ans = i
                    num = i
            
        return ans
n=6
arr = [4,67,13,17,15,18]
x=16
print(immediateGreater(arr,n,x))