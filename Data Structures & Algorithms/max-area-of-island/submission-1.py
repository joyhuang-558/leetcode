class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        res = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j]==1:
                    res = max(res,self.dfs(i,j))
        return res


    def dfs(self,i,j):
        #input: node if value == 1
        #output:area of this island start from this node 1
        if i<0 or i>=self.rows or j<0 or j>=self.cols:
            return 0
        if self.grid[i][j]==0:
            return 0
        else:
            self.grid[i][j]=0
            area = 1+self.dfs(i+1,j)+self.dfs(i,j+1)+self.dfs(i-1,j)+self.dfs(i,j-1)
        return area

        