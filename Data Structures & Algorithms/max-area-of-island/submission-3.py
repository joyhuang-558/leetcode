class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if grid[r][c]==0:
                return 0
            
            if (r,c) in visited:
                return 0

            visited.add((r,c))
            area = 1
            for dr,dc in directions:
                area+=dfs(r+dr,c+dc)
                #print(area)
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1 and (r,c) not in visited:
                    area = dfs(r,c)
                    max_area = max(max_area,area)
        return max_area
            
        