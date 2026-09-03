
'''
1. 状态定义
dp[i][s]：amount = s,使用从第0个到第i个num，包括本身i，一共有几种make up的方法
2. 转移方程

for i in range(1,len(nums)):
    num = nums[i]
    for s in 
    dp[i][s] = dp[i-1][s+num]+dp[i-1][s-num]

3. 初始状态
dp[0][nums[0]] += 1
dp[0][-nums[0]] += 1
4. 返回结果
dp[len(nums)-1][target]
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        dp = [[0]* (2*total+1) for _ in range(len(nums))]

        dp[0][nums[0]+total] += 1
        dp[0][-nums[0]+total] += 1

        

        for i in range(1,len(nums)):
            num = nums[i]
            for s in range(-total,total+1):
                s_index = s+total
                if 0<=s_index+num<=2*total:
                    dp[i][s_index]+= dp[i-1][s_index+num]
                if 0<=s_index-num<=2*total:
                    dp[i][s_index]+= dp[i-1][s_index-num]
                
        if 0<=target+total<=2*total:
            return dp[len(nums)-1][target+total]
        return 0

        