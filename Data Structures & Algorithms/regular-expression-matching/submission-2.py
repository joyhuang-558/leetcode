'''
1. dp定义
dp[i][j]表示s的前i个和p的前j个，是否能match，true or false
2. 转移方程
三种情况:
    s[i-1]==p[j-1] or p[j-1]==. 
    then dp[i][j]=dp[i-1][j-1]

    p[j-1]==*

    如果p[i-2]=s[i-1]或者，p[i-2]=*那么s继续往前看
    then dp[i][j]=dp[i-1][j]

    如果选择删除，dp[i][j]=dp[i][j-2]


3. 初始状态
dp[0][0]=True
dp[i][0]= False

dp[0][j]=dp[0][j-2] if p[j-1]=*
else False

4. 返回结果
dp[lens+1][lenp+1]
'''



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)

        dp = [[False]*(len_p+1) for _ in range(len_s+1)]

        dp[0][0]=True


        for j in range(2,len_p+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-2]
        
        for i in range(1,len_s+1):
            for j in range(1,len_p+1):
                if ((s[i-1]==p[j-1]) or (p[j-1]=='.')):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    #delete
                    dp[i][j] = dp[i][j-2] 
                    

                    if p[j-2]==s[i-1] or p[j-2]=='.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                    



        return dp[len_s][len_p]


        