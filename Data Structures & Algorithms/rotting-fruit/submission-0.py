class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = collections.deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh += 1
                elif grid[i][j]==2:
                    q.append((i,j))
    

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh>0:
            length = len(q)
            #在这一轮影响周围中
            for _ in range(length):
                i,j = q.popleft()
                for di,dj in directions:
                    row,col = i+di,j+dj
                    if (row in range(rows)and col in range(cols) and grid[row][col]==1):
                        grid[row][col]=2
                        fresh-=1
                        q.append((row,col))
            time+=1
        return time if fresh == 0 else -1
        



        