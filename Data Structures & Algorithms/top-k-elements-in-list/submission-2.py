class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num]=d.get(num,0)+1

        l = [[]for _ in range(len(nums)+1)]
        for num,f in d.items():
            l[f].append(num)
        res = []
        for i in range(len(l)-1,0,-1):
            if l[i]!=[]:
                for c in l[i]:
                    res.append(c)
                    if len(res)==k:
                        return res
            
      
