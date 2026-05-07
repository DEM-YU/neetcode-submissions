class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lengths = [1] * n

        left_lengths = 1
        for i in range(n):
           lengths[i] = left_lengths
           left_lengths *= nums[i]

        right_lengths = 1
        for i in range(n - 1, -1, -1):
            lengths[i] *= right_lengths 
            right_lengths *= nums[i]
        
        return lengths