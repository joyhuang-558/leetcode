class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp[i]表示以i结尾的最大，有两种可能，加上自己，只有自己
        #nums:2,-3,4,-2,2,1,-1,4
        #dp.  0, 0,0, 0,0,0, 0,0
        ans = -1000000
        dp = [0]*len(nums)
        for i,num in enumerate(nums):
            if i==0:
                dp[0] = num
            else:
                dp[i] = max(dp[i-1]+nums[i],nums[i])
            ans = max(ans,dp[i])
        return ans
        
