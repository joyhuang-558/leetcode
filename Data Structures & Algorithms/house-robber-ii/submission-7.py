class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo1 = [-1]*len(nums)
        memo2 = [-1]*len(nums)
        
        def dp(i,nums,index):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            if index == 1:
                if memo1[i] != -1:
                    return memo1[i]
                memo1[i] = max(dp(i-1,nums,index),dp(i-2,nums,index)+nums[i])
                return memo1[i]
            if index == 2:
                if memo2[i] != -1:
                    return memo2[i]
                memo2[i] = max(dp(i-1,nums,index),dp(i-2,nums,index)+nums[i])
                return memo2[i]

        n = len(nums)
        return max(dp(n-2,nums[0:n-1],1), dp(n-2,nums[1:n],2))
