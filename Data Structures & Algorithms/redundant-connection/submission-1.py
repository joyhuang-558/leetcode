class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.adj = [[] for _ in range(len(edges)+1)]
        for a,b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        self.visit = []
        self.parents = {} # node -> parent

        self.parents[1] = -1
        circle_node = self.dfs(1, -1)

        circle_list = []

        print(circle_node)

        cur_node = circle_node

        while True:
            circle_list.append((cur_node, self.parents[cur_node])) # tuple 

            cur_node = self.parents[cur_node]

            if cur_node == circle_node:
                break

        # inverse index 
        edge_index = {} # edge -> index

        # TODO: what can be a key and what cannot and why? Hashable

        for i, edge in enumerate(edges):
            edge_tuple = (edge[0], edge[1])
            edge_tuple_2 = (edge[1], edge[0])
            edge_index[edge_tuple] = i
            edge_index[edge_tuple_2] = i

        max_index = -1
        for edge in circle_list:
            index = edge_index[edge]
            if index > max_index:
                max_index = index

        return edges[max_index]

        




    #dfs目的：找到circle node
    def dfs(self,node,parent):
        self.visit.append(node)
        for nei in self.adj[node]:
            if nei == parent:
                continue

            if nei in self.visit:
                self.parents[nei] = node
                return nei
            else:
                self.visit.append(nei)
                self.parents[nei] = node
                res = self.dfs(nei, node)
                if res is not None:
                    return res

        
                
    

        