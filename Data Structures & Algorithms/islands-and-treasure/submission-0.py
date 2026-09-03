class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_inf = 0
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                if grid[i][j]==2147483647:
                    num_inf+=1
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        distance = 1
        while q and num_inf>0:
            length = len(q)
            for _ in range(length):
                i,j = q.popleft()
                for di,dj in d:
                    row = i+di
                    col = j+dj
                    if (row in range(rows)and col in range(cols)and grid[row][col]==2147483647):
                        num_inf-=1
                        grid[row][col]=distance
                        q.append((row,col))
                
            distance += 1
        
        return None


        