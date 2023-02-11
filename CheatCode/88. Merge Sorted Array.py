def merge(nums1, nums2):
    m=len(nums1)
    n=len(nums2)
    nums1[m:] = nums2[:n]
    print(nums1[m:])
    print(nums2[:n])
    print(nums1[m:] = nums2[:n])
    return sorted(nums1)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

print(merge(nums1, nums2))