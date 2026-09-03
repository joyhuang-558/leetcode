class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]以i结尾的最长increase的arry数量
        #转移：如果dp[i]>max 前面，就是说比前面的最长increase的arry的max大，就append进去
        #转移，else，就从自己开始。
        # dp 0 = 自己
        ans = 1
        dp = [1]*len(nums)
        for i,num in enumerate(nums):
            for j in range(i):
                #print(f"i:{i},j:{j}")
                cur = 0
                if nums[j]<nums[i]:
                    cur = max(dp[j]+1,cur)
                dp[i]=max(cur,dp[i])
                #print(f"dp[{i}]:{dp[i]}")
            ans = max(ans,dp[i])
        return ans
        
