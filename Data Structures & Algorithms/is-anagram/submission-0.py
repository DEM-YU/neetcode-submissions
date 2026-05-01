class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for i in s:
            if i in counts:
                counts[i] = counts[i] + 1 
            else: 
                counts[i] = 1 
        for j in t:
            if j in counts:
                counts[j] = counts[j] - 1
            else:
                return False
        for key in counts:
            if counts[key] != 0:
                return False
        
        return True
