class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            if tuple(sorted(i)) in d:
                d[tuple(sorted(i))].append(i)
            else:
                d[tuple(sorted(i))] = [i]
        res_ls = []
        for value in d.values():
            res_ls.append(value)
        return res_ls
            
        