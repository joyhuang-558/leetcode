class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dp[i]:包括自己在内，目前最大和最小的res
        #转移方程：自己，自己和之前最大，最小的res，并且更新。然后全局有一个最大。
        ans = -10000
        dp = [[0,0,0] for _ in range(len(nums))]
        dp[0]=[nums[0],nums[0],nums[0]]
        if len(nums)==1:
            return nums[0]
        #print(dp)
        for i in range(1,len(nums)):
            dp[i][0] = nums[i]
            dp[i][1] = max(nums[i],nums[i]*dp[i-1][1],nums[i]*dp[i-1][2])
            dp[i][2] = min(nums[i],nums[i]*dp[i-1][1],nums[i]*dp[i-1][2])
            #print(dp)
            ans = max(ans,max(dp[i][0],dp[i][1],dp[i][2]))
            #print(ans)
        return ans
        