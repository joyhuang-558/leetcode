class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        need = {}
        for i in t:
            need[i] = need.get(i,0)+1
        valid = 0
        length = float('inf')
        window = {}
        start = 0

        while right < len(s):
            cur = s[right]
            right += 1
            if cur in need:
                window[cur] = window.get(cur,0)+1

                if window[cur]==need[cur]:
                    valid += 1
            
            while left < right and valid ==len(need):
                if right-left<length:
                    start = left
                    length = right-left

                cur = s[left]
                left  += 1
                if cur in need:
                    if window[cur]==need[cur]:
                        valid-=1
                    window[cur]-=1
        return "" if length==float('inf') else s[start:start+length]
                    









        