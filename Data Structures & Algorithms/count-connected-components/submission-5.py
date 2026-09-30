class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False]*n

        count = 0

        def dfs(node):
            visited[node]=True

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        
        for node in range(n):
            if visited[node]==False:
                count += 1
                dfs(node)

        return count

        