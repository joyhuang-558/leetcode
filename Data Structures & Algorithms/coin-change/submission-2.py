class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1]* (amount+1)
        def dp(i):
            if i == 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            res = float('inf')
            for m in coins:
                if i>=m:
                    res = min(res,dp(i-m)+1)
                else:
                    continue
            memo[i] = res
            return memo[i]
        return -1 if dp(amount) == float('inf') else dp(amount)
        