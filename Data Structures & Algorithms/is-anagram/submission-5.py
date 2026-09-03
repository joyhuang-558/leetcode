class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_s = self.set_s(s)
        res_t = self.set_s(t)
        return res_s==res_t and len(s)==len(t)

    def set_s(self,s):
        res = set()
        for c in s:
            res.add(c)
        return res
    

    
        