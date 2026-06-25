class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for i in strs:
            j = "".join(sorted(i))
            res[j].append(i)
        return list(res.values())    