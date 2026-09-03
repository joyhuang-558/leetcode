class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #dp[i]表示，是否可以凑出i
        #nums = 1 2 3 4
        #dp = t f f f f f
        #i    0 1 2 3 4 5
        #target = 5
        #
        total = sum(nums)
        if total%2 != 0:
            return False
        else:
            target = total//2
        print(f"target = {target}")
        
        dp = [False]*(target+1)
        dp[0]=True
        for num in nums:
            for i in range(target,num-1,-1):
                dp[i]=dp[i] or dp[i-num]
        return dp[target]
 
        
                    

                

        