class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i]表示，到第i个地方可以有多少种climb的方法
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
        
