class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return 0
        #两种结果，一个是偷头不偷尾，一个是偷尾不偷头，然后取max
        a = self.help(nums[:-1])
        b = self.help(nums[1:])
        return max(a,b)

    def help(self,nums):
        n = len(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return 0
        dp = [0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
        
