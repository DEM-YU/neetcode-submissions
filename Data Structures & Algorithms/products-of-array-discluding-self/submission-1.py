class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lengths = [1] * len(nums)

        left_lengths = 1
        for i in range(len(nums)):
            lengths[i] = left_lengths
            left_lengths *= nums[i]

        right_lengths = 1
        for i in range(len(nums) - 1, -1, -1):
            lengths[i] *= right_lengths
            right_lengths *= nums[i]
        
        return lengths
        