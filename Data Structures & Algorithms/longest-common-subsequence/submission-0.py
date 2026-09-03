
'''
1. 状态：dp[i][j]表示text1 前i位和text2前j位max多大。不包括本身这一位，需要比较
2. 转移方程：有两个结果，如果i j same就+1， 不然就same

dp[i][j] = if text1[i]==text2[j] than dp[i][j] = dp[i-1][j-1] +1, else 
dp[i][j] = max(
    dp[i-1][j],
    dp[i][j-1]
)

3. 初始状态，dp[0][0]，就是看第一位是否相等，是就1 不是就0
4. 返回结果，因为遍历所有的i和j，就直接返回dp[i][j],然后这个i和j表示len，就是比index 多1
'''

class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len1][len2]

        
        