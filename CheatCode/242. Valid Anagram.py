class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1,l2 = {}, {}

        for x in range(len(s)):
            l1[s[x]] = l1.get(s[x],0) +1
            l2[t[x]] = l2.get(t[x],0) +1
 
        return l1 == l2 

