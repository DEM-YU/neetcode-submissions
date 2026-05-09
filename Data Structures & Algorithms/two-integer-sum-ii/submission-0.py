class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_number = numbers[left] + numbers[right]
            
            if current_number == target:
                return[left + 1, right + 1]
            elif current_number < target:
                left = left + 1
            else:
                right = right - 1