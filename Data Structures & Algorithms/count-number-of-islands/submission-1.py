class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visit = [[False]*self.cols for _ in range(self.rows)]
        self.res = 0
        self.grid = grid
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.visit[i][j] and self.grid[i][j]=='1':
                    self.res+=1
                    self.dfs(i,j)
        return self.res

    def dfs(self,i,j):
        # when to stop: 1. out of range. 2.have been visited. 3. 0
        if i<0 or i >=self.rows or j<0 or j>=self.cols:
            return
        if self.visit[i][j]==True:
            return
        if self.grid[i][j]=='0':
            return
        self.visit[i][j]=True
        self.dfs(i+1,j)
        self.dfs(i,j+1)
        self.dfs(i-1,j)
        self.dfs(i,j-1)

        