class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ans = []
        #i:第i个nums
        def dfs(i,remain):
            if remain < 0 or i > len(nums)-1:
                return 

            elif remain == 0:
                res.append(ans.copy())
                return 

            #不选i
            dfs(i+1,remain)
            #选i
            ans.append(nums[i])
            dfs(i,remain-nums[i])
            ans.pop()
        dfs(0,target)
        return res
            
        
        

        
