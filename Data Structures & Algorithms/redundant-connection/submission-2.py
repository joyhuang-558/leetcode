class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #1. dfs找到成环的这个点。2. 每一步记录parent。3. 找到成环的这个点，开始往回追溯，记录每一条边，until parent是这个成环的点。4. 搞一个dic记录查询这个边。5. 按照index从小到大搞。
        self.adj = [[] for _ in range(len(edges)+1)]
        self.visited = [False]*(len(edges)+1)
        for a,b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        self.parents = {}
        self.parents[1]=0
        res = self.dfs(1,0)
        circle_list = []
        cur_node = res
        while True:
            circle_list.append((cur_node,self.parents[cur_node]))
            cur_node = self.parents[cur_node]
            if cur_node == res:
                break
        d = {}
        for i,edge in enumerate(edges):
            edge_tuple1 = (edge[0],edge[1])
            edge_tuple2 = (edge[1],edge[0])
            d[edge_tuple1]=i
            d[edge_tuple2]=i
        
        index = -1
        print(circle_list)
        for i in circle_list:
            index = max(index,d[i])
        return edges[index]






    def dfs(self,node,parent):

        self.visited[node]=True

        for nei in self.adj[node]:
            if nei == parent:
                continue
            if self.visited[nei]==True:
                self.parents[nei]=node
                return nei
            else:
                self.parents[nei]=node
                res = self.dfs(nei,node)
                if res is not None:
                    return res
        return None
    


        