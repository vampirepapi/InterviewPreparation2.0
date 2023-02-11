# Naive Approach
# def threeSum(nums):
#     ans =[]
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             for k in range(j+1,len(nums)):
#                 if nums[i]+nums[j]+nums[k] == 0:
#                     res =  nums[i],nums[j],nums[k]
#                     ans.append(res)
#     return set(ans)

def threeSum(nums):
    nums.sort()
    def getTwoSum(arr,target,numsOfI,ansArr):
        p1=0
        p2=len(arr)-1
        while p1<p2:
            if arr[p1]+arr[p2] == target:
                # return [arr[p1],arr[p2]]
                # print(arr[p1],arr[p2],target,numsOfI)
                # print(nums[p1],nums[p2])
                # print(arr)
                # print(nums)
                ans.append([arr[p1],arr[p2],numsOfI])
                p2-=1

            elif arr[p1]+arr[p2] > target:
                p2-=1
            
            else:
                p1+=1
        
        return ans
    
    i=0
    # result = []
    ans=[]
    while i<len(nums):
        newTarget = -nums[i]
        start = i+1
        end = len(nums)
        ans = getTwoSum(nums[start:end], newTarget, nums[i], ans)
        # if listOfTwoNums is not None:
        #     listOfTwoNums.append(nums[i])
        #     result.append(tuple(listOfTwoNums))
        i+=1

    return ans	




nums = [-2,0,1,1,2]
print(threeSum(nums))