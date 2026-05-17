class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            current_width = right - left
            current_height = min(heights[left], heights[right])
            current_water = current_width * current_height
            max_water = max(max_water, current_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_water