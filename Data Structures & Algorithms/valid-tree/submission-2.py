class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adj = [[] for _ in range(n)]
        for a,b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        self.visited = []
        self.n = n
        if not self.dfs(0, -1):
            return False
        if len(self.visited)==n:
            return True
        return False
    def dfs(self,node,parent):
        self.visited.append(node)
        for nei in self.adj[node]:
            if nei==parent:
                continue 
            if nei in self.visited:
                return False
            if not self.dfs(nei,node):
                return False
        return True
        

        