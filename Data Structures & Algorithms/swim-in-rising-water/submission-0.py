class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 目的：从左上角走到右下角，过最小的时间
        # 规则：time时间可以经过小于等于time高度的柱子
        # 维护一个heap，从左上角开始，每次扩展上下左右（合法的），加入heap，然后while到达右下角，中间每次都pop出来高度最小的。然后更新这个time，取max time和这个高度。
        #记得加一个visited，不然会重复
        #heap: (grid[i][j],i,j)
        time = 0
        n = len(grid)
        h = []
        h.append([grid[0][0],0,0])
        ds = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = [[False]*n for _ in range(n)]
        visited[0][0]=True
        while h:
            cur_h,i,j = heapq.heappop(h)
            time = max(time,cur_h)
            if i == n-1 and j == n-1:
                return max(time,cur_h)

            for di,dj in ds:
                new_i = i+di
                new_j = j+dj

                if (new_i in range(n) and new_j in range(n)):
                    if visited[new_i][new_j] == False:
                        heapq.heappush(h,[grid[new_i][new_j],new_i,new_j])
                        visited[new_i][new_j] = True
                else:
                    continue
                
        return time







        