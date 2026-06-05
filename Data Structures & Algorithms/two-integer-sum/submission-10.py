class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        for i in range(len(nums)):
            val = nums[i]
            diff =  target - val

            if diff in set:
                return[set[diff], i]
            set[val] = i
        return[]
    
        