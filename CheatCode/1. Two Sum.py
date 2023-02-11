# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return i,j

# TC = O(n**2)

# as the tc of above solution isnt optimized so we have to solve this in good tc
def twoSum(nums, target):
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

nums = [3,2,4]
target = 6

print(twoSum(nums, target))