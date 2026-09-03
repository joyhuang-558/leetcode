class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                elif board[i][j] not in row_set:
                    row_set.add(board[i][j])
                else:
                    return False


        for j in range(9):
            col_set = set()
            for i in range(9):
                if board[i][j]=='.':
                    continue
                elif board[i][j] not in col_set:
                    col_set.add(board[i][j])
                else:
                    return False

        for square in range(9):
            square_set = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j
                    if board[row][col]=='.':
                        continue
                    elif board[row][col] not in square_set:
                        square_set.add(board[row][col])
                    else:
                        return False     
        return True          
                    
        



        
