class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub_res = []

        def dfs(i):
            if sum(sub_res) == target:
                res.append(sub_res.copy())
                return
            if i >=len(nums)or sum(sub_res) > target:
                return
            sub_res.append(nums[i])
            dfs(i)
            sub_res.pop()
            dfs(i+1)
        
        dfs(0)
        return res

        