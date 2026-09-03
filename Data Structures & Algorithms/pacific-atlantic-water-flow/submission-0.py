class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        p_queue = collections.deque()
        a_queue = collections.deque()
        p_visited = set()
        a_visited = set()
        self.rows = len(heights)
        self.cols = len(heights[0])

        for i in range(self.rows):
            p_queue.append((i,0))
            p_visited.add((i,0))
        for j in range(self.cols):
            p_queue.append((0,j))
            p_visited.add((0,j))
        for i in range(self.rows):
            a_queue.append((i,self.cols-1))
            a_visited.add((i,self.cols-1))
        for j in range(self.cols):
            a_queue.append((self.rows-1,j))
            a_visited.add((self.rows-1,j))
        self.bfs(p_queue,p_visited)
        self.bfs(a_queue,a_visited)
        common = p_visited & a_visited
        l_common = [i for i in common]
        return l_common
    def bfs(self,queue, visited):
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            length = len(queue)
            for _ in range(length):
                i,j = queue.popleft()
                for di,dj in d:
                    row = i+di
                    col = j+dj
                    if (row in range(self.rows) and col in range(self.cols)and self.heights[row][col]>=self.heights[i][j]and (row,col) not in visited):
                        queue.append((row,col))
                        visited.add((row,col))




        