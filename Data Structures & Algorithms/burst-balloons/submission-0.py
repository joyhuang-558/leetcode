class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        full_nums = [1]+nums+[1]
        
        dp=[[0]*(len(full_nums))for _ in range(len(full_nums))]

        n = len(full_nums)
        for length in range(2,n):
            for left in range(0,n-length):
                right = left+length

                for k in range(left+1,right):
                    value = dp[left][k]+full_nums[left] * full_nums[k] * full_nums[right]+dp[k][right]
                    dp[left][right]=max(value,dp[left][right])
        
        return dp[0][n-1]




        