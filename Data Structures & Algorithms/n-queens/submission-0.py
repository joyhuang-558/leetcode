class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.board = [['.']*n for _ in range(n)]
        self.res = []
        self.backtrack(0)
        return self.res
    def isValid(self,row,col):
        #up
        for i in range(row):
            if self.board[i][col]=='Q':
                return False
        #upleft
        i = row-1
        j = col-1
        while i>=0 and j>=0:
            if self.board[i][j]=='Q':
                return False
            i-=1
            j-=1
        #upright
        i = row-1
        j = col+1
        while i>=0 and j<self.n:
            if self.board[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True



    def backtrack(self,row):
        if row==self.n:
            sol = [''.join(r)for r in self.board]
            self.res.append(sol)
            return
        for col in range(self.n):
            if not self.isValid(row,col):
                continue
            else:
                self.board[row][col]='Q'
                self.backtrack(row+1)
                self.board[row][col]='.'
                



        