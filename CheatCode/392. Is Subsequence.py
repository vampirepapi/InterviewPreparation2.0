# The idea is to use two pointers, one pointer will start from start of str1 and another will start from start of str2. If current character on both the indexes are same then increment both pointers otherwise increment the pointer which is pointing str2. 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        n,m = len(s),len(t)

        while i<n and j<m:
            if s[i] == t[j]:
                i+=1
            j+=1
        return i==n
        
# Time Complexity: O(max(n,m)), where n,m are the length of given string s1 and s2 respectively. 
# Auxiliary Space: O(1) 