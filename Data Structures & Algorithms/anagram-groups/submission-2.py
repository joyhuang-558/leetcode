class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        for k,v in d.items():
            res.append(v)
        return res

        