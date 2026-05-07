class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            j = "".join(sorted(s))
            res[j].append(s)
        return list(res.values())