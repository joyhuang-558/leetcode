
'''
1. dp定义 dp[i][j]表示，word1的前i个，word2的前j，前面都match，min的步数。不包括自身。
2. 转移方程 dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
因为insert，delete，change，改动次数都是1
3. 初始状态
dp[0][0] = 0,因为不包括本身，所以是空字符串
dp[i][0] = i
dp[0][j] = j
4. 返回结果
如果i 大于等于len1-1了，就返回dp[i][j]+剩下的word2部分
如果j大于等于len2-1了，就返回dp[i][j]+剩下的word1部分
dp[i][j]


题目要返回min number change，until word1和word2完全一样。
完全一样means，length一样 ，每一个index一样。
i，j是word1和word2的两个index
分别遍历。
碰到不一样的，word1有三个选择，加，删，改。分别这三个选择各自继续往下，until，i out of range了。走完了，并且这个时候word2还没搞完。所以剩下的直接append就好。

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        dp = [[10000]*(len2+1) for _ in range(len1+1)]
        dp[0][0]=0
        for i in range(len1+1):
            for j in range(len2+1):
                dp[0][j]=j
                dp[i][0]=i
        
        for i in range(1,len1+1):
            for j in range(1,len2+1):    
                if word1[i-1]!= word2[j-1]:
                    cost = 1
                else:
                    cost = 0
                dp[i][j]= min(min(dp[i-1][j],dp[i][j-1])+1, dp[i-1][j-1]+cost)
        
        return dp[len1][len2]
                


        