class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            current_width = right - left
            current_heights = min(heights[left], heights[right])
            current_area = current_width * current_heights
            max_water = max(current_area, max_water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_water