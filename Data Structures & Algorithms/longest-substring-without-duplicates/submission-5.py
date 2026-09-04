class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        l=0
        
        cur_set = set()
        
        
        for r in range(len(s)):
            if s[r] not in cur_set:
                cur_set.add(s[r])
              
                res = max(res,r-l+1)
                
            else:
                while s[r] in cur_set:
                    cur_set.remove(s[l])
                   
                    l+=1
                cur_set.add(s[r])
                res = max(res,r-l+1)
        return res
        

            





        