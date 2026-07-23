class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = {}

        for i in s:
            if i not in count_1:
                count_1[i] = 1
            else:
                count_1[i] += 1
        
        count_2 = {}

        for j in t:
            if j not in count_2:
                count_2[j] = 1
            else:
                count_2[j] += 1
        
        if count_1 == count_2:
            return True
        
        return False


