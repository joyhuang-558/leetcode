class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resl = resr = 0
        for i in range(n):
            l = r = i
            while l >=0 and r < n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1 > resr-resl+1:
                resl = l+1
                resr = r-1

        

        for i in range(n-1):
            l = i
            r = i+1
            while l >=0 and r < n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1 > resr-resl+1:
        
                resl = l+1
                resr = r-1

        
        return s[resl:resr+1]
            
                

                
            