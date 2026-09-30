class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        start = 0
        max_len = 0

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                # print(f"i = {i}")
                # print(f"j = {j}")
                if s[i]==s[j]:
                    if j-i<=2 or dp[i+1][j-1]:
                        dp[i][j]=True
                
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    start = i
        return s[start:start+max_len]
        


        