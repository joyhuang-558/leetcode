class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        words = set()
        m,n = len(board),len(board[0])
        def dfs(x,y,i):
            #x,y are the position of cell
            #i is the position of the wors

            if i >len(word)-1 or x>m-1 or y>n-1 or x<0 or y<0 or (x,y) in words or board[x][y] != word[i]:
                return False
            if i == len(word)-1 and board[x][y] == word[i]:
                return True

            if board[x][y] == word[i]:
                words.add((x,y))
                
            remain = (dfs(x+1,y,i+1) or
                     dfs(x-1,y,i+1) or
                     dfs(x,y+1,i+1) or
                     dfs(x,y-1,i+1))
            
            words.remove((x,y))
            return remain
        
        for x in range(m):
            for y in range(n):
                if dfs(x,y,0):
                    return True
        return False
            

            
            
            
            

        