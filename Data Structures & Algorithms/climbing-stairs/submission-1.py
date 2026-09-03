class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            else:
                return dfs(i-1)+dfs(i-2)
        
        return dfs(n)

        