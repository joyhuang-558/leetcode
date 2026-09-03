import collections
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = collections.deque()
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            if board[i][0]=="O":
                q.append((i,0))
            if board[i][cols-1]=="O":
                q.append((i,cols-1))
        for j in range(cols):
            if board[0][j]=="O":
                q.append((0,j))
            if board[rows-1][j]=="O":
                q.append((rows-1,j))

        d = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            i,j = q.popleft()
            board[i][j]="1"
            for di,dj in d:
                row = i+di
                col = j+dj
                if (row in range(rows) and col in range(cols) and board[row][col]=="O"):
                    board[row][col]="1"
                    q.append((row,col))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] =="O":
                    board[i][j]="X"
                if board[i][j] =="1":
                    board[i][j]="O"





        


        
