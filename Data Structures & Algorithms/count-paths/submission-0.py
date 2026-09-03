
'''
1. 状态定义
dp[i][j]表示the number of possible unique paths，走到这一步
dp = [[0]*n for _ in range(m)]
2. 转移方程
有两个方向来当前这个格子，从上往下，从左往右
dp[i][j] = dp[i-1][j+dp[i][j-1]
3. 初始状态
最上一排和最左一列都是1种，dp[0][j]=1,dp[i][0]=1
4， 返回结果
dp[m-1][n-1]
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
              
        