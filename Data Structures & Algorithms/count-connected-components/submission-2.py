class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited = []
        self.adj = [[] for _ in range(n)]
        res = 0
        if len(edges)==0:
            return 0
        for a,b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        for i in range(n):
            if i not in self.visited:
                res+=1
                self.dfs(i,-1)
        return res

    #这个dfs负责，走遍这个所有的联通的,并且标记走过的为visited
    def dfs(self,node,parent):
        for nei in self.adj[node]:
            if nei in self.visited:
                continue
            self.visited.append(nei)
            self.dfs(nei,node)



        