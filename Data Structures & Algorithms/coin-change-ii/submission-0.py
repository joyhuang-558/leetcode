
'''
1. dp意义
dp[i]表示要make amount i 所有的解法
dp = [0]* (amount+1)

2. 转移方程
for coin in coins:
    for i in range(coin,amount+1)
        dp[i]+=dp[i-coin]

3. 初始状态
dp[0]=1

4. 返回结果
dp[amount]
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]* (amount+1)

        dp[0]=1

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]+=dp[i-coin]
        return dp[amount]
