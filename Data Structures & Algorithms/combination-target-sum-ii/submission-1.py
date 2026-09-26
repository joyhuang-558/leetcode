class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(i):
            if sum(path)==target:
                res.append(path.copy())
                return            
            if i>=len(candidates) or sum(path)>target:
                return

            #选择
            path.append(candidates[i])
            dfs(i+1)
            #不选择
            path.pop()
            next_i = i+1
            while next_i <len(candidates) and candidates[next_i]==candidates[i]:
                next_i+=1
            dfs(next_i)
        dfs(0)
        return res
        