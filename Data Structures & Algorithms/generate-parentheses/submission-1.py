class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(left_count,right_count):
            if left_count == n and right_count == n:
                res.append("".join(path))
            
            if left_count<n:
                path.append("(")
                dfs(left_count+1,right_count)
                path.pop()
            if right_count<left_count:
                path.append(")")
                dfs(left_count,right_count+1)
                path.pop()
        
        dfs(0,0)

        return res

        
        