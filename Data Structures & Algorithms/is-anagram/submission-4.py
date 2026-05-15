class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        count2 = {}
        for j in t:
            if j not in count2:
                count2[j] = 1
            else:
                count2[j] += 1
        
        if count == count2:
            return True
        return False
