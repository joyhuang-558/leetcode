class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #思路是用bfs来做，然后控制一个次数，如果这个次数大于k就break，此时看是否满足，如果没有一个满足就返回false。然后之前满足的，每次都加入res，最后看res的min。
        #这个dic：start-[[end1,dis1],[end2,dis2]]
        #q里面放，这一层可以走的node
        #每走完完整一层，就+1
        #然后看这里面的nei，然后如果nei是end，更新res，放进去这个res list里面
        #有个问题想不明白，就是说，这个res，每个都不一样并且要累加，怎么做到？
        #回答：这个q里面不仅要装node，还要装cost，不在乎start，因为就表示，此刻合法走到这个点，cost是多少。
        dic = defaultdict(list)
        for flight in flights:
            start = flight[0]
            end = flight[1]
            distance = flight[2]
            dic[start].append([end,distance])

        #需要记录一下每个node 的min cost
        min_cost = {}
        min_cost[src]=0

        q = deque()
        q.append((src,0))
        #num表示：到目前这层的node，已经从src走了num条边。题目要求是中间有k个node，也就是最多走k+1条边
        num = 0
        res = 100000
        #num对于每一层都是一样的，判断的时候在进入这个层之前做
        while q:
            lenght = len(q)
            #说明到这一层已经满了无法扩展了
            if num==k+1:
                break

            for _ in range(lenght):
                
                cur,cur_cost = q.popleft()

                for node,cost in dic[cur]:
                    new_cost = cost+cur_cost
                    if node in min_cost and min_cost[node]<=new_cost:
                        continue
                    else:
                        q.append((node,new_cost))
                        min_cost[node] = new_cost
                    if node == dst:
                        res = min(res,new_cost)

            num+=1
        return -1 if res==100000 else res


                    





        