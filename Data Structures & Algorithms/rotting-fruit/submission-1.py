class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()

        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        
        while queue:
            layer_size = len(queue)

            for _ in range(layer_size):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr = dr+r
                    nc = dc+c

                    if nr<0 or nr>=rows or nc<0 or nc>=cols:
                        continue
                    
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        queue.append((nr,nc))
            print(queue)
            print(time)
            time+=1
        
        return time-1 if fresh==0 else -1
        