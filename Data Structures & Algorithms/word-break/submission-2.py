class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i]表示i这个地方之前，是否true
        #s =   l e e t c o d e
        #. =   0 1 2 3 4 5 6 7
        #dp= 0 1 2 3 4 5 6 7 8 
        
        n = len(s)
        dp = [False]*(n+1)
        dp[0]=True
        for i in range(0,n+1):
            #print(f"i = {i}")
            for j in range(0,i):
                #print(f"i = {i}, j = {j}")
                #print(f"dp[:j]=:{dp[:j]} s[j:i]= {s[j:i]}")
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                #print(f"dp[{i}]={dp[i]}")
        return dp[-1]

        