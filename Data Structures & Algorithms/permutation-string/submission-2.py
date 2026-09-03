class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right = 0
        left = 0
        need = {}
        valid = 0
        for i in s1:
            need[i] = need.get(i,0)+1
        window = {}
        while right < len(s2):
            cur = s2[right]
            right += 1
            if cur in need:
                window[cur] = window.get(cur,0)+1
                if window[cur] == need[cur]:
                    valid += 1

            while right-left>len(s1):
                d = s2[left]
                left += 1
                if d in need:
                    if need[d]==window[d]:
                        valid -= 1
                    window[d] -= 1
            if valid == len(need):
                return True
        return False
            
            
        