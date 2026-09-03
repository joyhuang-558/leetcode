'''
1. dp定义
dp[i][j]表示，s1的前i位置和s2的前j位置，拼起来。能否拼成s3的前i+j。
dp[i] = 前 i 个
当前字符 = string[i-1]

2. 转移方程
dp[i][j]=
dp[i-1][j] and s1[i-1]==s3[i+j-1]
or
dp[i][j-1] and s2[j-1]==s3[i+j-1]


3. 初始状态
dp[0][0]=True
dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
4. 返回结果
dp[len1][len2]
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False]*(len2+1) for _ in range(len1+1)]

        dp[0][0]=True

        for i in range(1,len1+1):
            dp[i][0] = dp[i-1][0] and s3[i-1]==s1[i-1]

        for j in range(1,len2+1):
            dp[0][j] = dp[0][j-1] and s3[j-1]==s2[j-1]

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                dp[i][j]=(
                    (dp[i-1][j] and s3[i+j-1]==s1[i-1])
                    or
                    (dp[i][j-1] and s3[i+j-1]==s2[j-1])
                    )
        return dp[len1][len2]


        