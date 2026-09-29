class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c))
        
        def is_land(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            return grid[r][c]==INF
        
        while queue:
            r,c = queue.popleft()
            cur_dist = grid[r][c]

            for dr,dc in directions:
                nr = dr+r
                nc = dc+c
                if is_land(nr,nc):
                    grid[nr][nc] = 1+cur_dist
                    queue.append((nr,nc))
        

        