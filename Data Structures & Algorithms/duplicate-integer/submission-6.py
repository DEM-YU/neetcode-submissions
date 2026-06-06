class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if count.get(i,0) >=1 :
                return True
            count[i] = count.get(i,0) + 1
        return False
        

        