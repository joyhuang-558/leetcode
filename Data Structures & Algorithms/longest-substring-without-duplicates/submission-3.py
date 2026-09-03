class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        window = {}
        max_len = 0

        while right < len(s):
            cur = s[right]
            right += 1
            window[cur] = window.get(cur,0)+1

            while window[cur]>1:
                d = s[left]
                window[d]-=1
                left += 1
            
            max_len = max(right-left,max_len)

        return max_len 

                

        