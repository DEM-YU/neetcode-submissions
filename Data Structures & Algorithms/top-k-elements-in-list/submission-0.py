class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] = counts[i] + 1
            else:
                counts[i] = 1

        pairs = []
        for key in counts:
            pairs.append([key, counts[key]])

        n_pairs = len(pairs)
        for i in range(n_pairs):
            for j in range(0, n_pairs - i - 1):
                if pairs[j][1] < pairs[j + 1][1]:
                    temp = pairs[j]
                    pairs[j] = pairs[j + 1]
                    pairs[j + 1] = temp

        result = []
        for i in range(k):
            result.append(pairs[i][0])
            
        return result