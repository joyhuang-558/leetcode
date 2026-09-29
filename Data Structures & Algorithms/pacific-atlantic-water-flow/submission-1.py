class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c,visited,pre_h):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            
            if (r,c) in visited:
                return
            if heights[r][c]<pre_h:
                return
            
            visited.add((r,c))

            for dr,dc in directions:
                nr = dr+r
                nc = dc+c
                dfs(nr,nc,visited,heights[r][c])
        
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])

        for c in range(cols):
            dfs(rows-1,c,atlantic,heights[rows-1][c])
        for r in range(rows):
            dfs(r,cols-1,atlantic,heights[r][cols-1])
        
        res = []
        for r,c in atlantic & pacific:
            res.append([r,c])
        
        return res
        

        