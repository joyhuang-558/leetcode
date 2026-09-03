class Solution:
    def numDecodings(self, s: str) -> int:
        #dp[i]:从0-i一共多少种decode的方式
        dp = [0]*len(s)

        dp[0] = 0 if int(s[0])==0 else 1


        if len(s)>=2:
            if int(s[1])!=0:
                dp[1]+=dp[0]
            if (10<=int(s[0:2])<=26):
                dp[1]+=1
            print(dp)

        for i in range(2,len(s)):
            #情况1:自己单独
            if int(s[i])!=0:
                dp[i]+=dp[i-1]
            #情况2:和前面的组队,但是要确保两个组合起来在10-26之间
            if 10<=int(s[i-1:i+1])<=26:
                dp[i]+=dp[i-2]
        return dp[-1]


        