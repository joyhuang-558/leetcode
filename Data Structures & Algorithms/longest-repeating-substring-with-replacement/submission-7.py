class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        res = 0
        window = {}
        while right < len(s):
            cur = s[right]
            right += 1
            window[cur] = window.get(cur,0)+1
            
            cur_max = max(window.values())
            while right-left>cur_max+k:
                d = s[left]
                left += 1
                window[d]-=1
            
            res = max(res,right-left)
            
        return res
            



            



        