class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #1. 先把所有的node到其他人node的距离算出来。这个用dic储存，就是node--[nei，distance]
        #2. 创建一个heap，h，然后从任意一个点出发，遍历这个点的nei，加入heap。heap里面存[distance，node]，其中这个distance是当前这个点到nei到distance，也就是目前为止已经成了的tree整个整体到这个node的距离。
        #3. 然后pop出来一个node，需要记录visited。然后heap就不要在访问这样了。
        #4. 最后返回这个res。res一开始=0，然后pop出来后一个就加上这个distance。

        #注意，这个node如何表示也是个问题，我想的是，用这个points里面的index表示，然后坐标就是points[index]
        visited = set()
        
        dic = defaultdict(list)
        for i,x in enumerate(points):
            for j,y in enumerate(points):
                if x==y:
                    continue
                else:
                    dic[i].append([j,self.cal_distance(x,y)])
        h = []
        heapq.heappush(h,(0,0))


        res = 0
        while h:
            cur_dis,cur_node = heapq.heappop(h)
            #print(f"cur_dis,cur_node = {cur_dis}, {cur_node}")
            if cur_node in visited:
                continue
            else:
                res += cur_dis
                #print(f"res = {res}")
                visited.add(cur_node)
            for nei,dis in dic[cur_node]:
                heapq.heappush(h,(dis,nei))
                #print(f"heap {h}")
        
        return res

    
    def cal_distance(self,x,y):
        distance = abs(x[0]-y[0])+abs(x[1]-y[1])
        return distance
        