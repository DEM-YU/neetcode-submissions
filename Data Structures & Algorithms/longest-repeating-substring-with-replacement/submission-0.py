class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        max_count = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(count[s[right]], max_count)

            while (right - left +1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left +1)

        return res
    
    
