class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        pre_min = 0
        cur = 0

        for i in nums:
            cur += i
            ans = max(ans,cur - pre_min)
            pre_min = min(cur,pre_min)
        return ans





        
        