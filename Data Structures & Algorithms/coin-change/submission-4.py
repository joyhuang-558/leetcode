class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for i,amount in enumerate(dp):
            print(f"i{i},amount{amount}")
            for coin in coins:
                print(f"coin{coin}")
                if coin<=i:
                    dp[i]= min(dp[i-coin]+1,dp[i])
                    print(f"dp[i]{dp[i]}")
        return dp[-1] if dp[-1]!=float('inf') else -1

        