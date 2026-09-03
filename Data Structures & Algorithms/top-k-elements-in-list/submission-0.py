class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 0
        
        ls = sorted([i for i in d.values()],reverse = True)
        index = ls[:k]
        res = []
        for key,value in d.items():
            if value in index:
                res.append(key)
        return res


        