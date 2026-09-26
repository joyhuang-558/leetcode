class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_res = []

        def dfs(i):
            if i >= len(nums):
                res.append(sub_res.copy())
                return
            
            sub_res.append(nums[i])
            dfs(i+1)
            sub_res.pop()
            dfs(i+1)
        dfs(0)
        return res

        