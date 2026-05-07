class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i] ,0) + 1
            count[t[i]] = count.get(t[i] ,0) - 1
        
        for j in count.values():
            if j != 0:
                return False
        return True
