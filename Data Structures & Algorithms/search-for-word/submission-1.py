class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        row_num = len(board)
        col_num = len(board[0])
        used = [[False]*col_num for _ in range(row_num)]

        def dfs(x,y,i):
            if x<0 or x>=row_num or y<0 or y>=col_num or used[x][y] or board[x][y] != word[i]:
                return False
            if i==len(word)-1:
                return True
            

            used[x][y]=True
            for d in directions:
                new_x = d[0]+x
                new_y = d[1]+y
                if dfs(new_x,new_y,i+1):
                    return True
            
            used[x][y]=False
            return False
        
        for x in range(row_num):
            for y in range(col_num):
                if dfs(x,y,0):
                    return True
        return False



                    
                    

        