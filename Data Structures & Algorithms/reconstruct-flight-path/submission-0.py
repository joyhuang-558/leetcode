
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #构造一个adj dic
        self.adj = defaultdict(list)
        for ticket in tickets:
            heapq.heappush(self.adj[ticket[0]],ticket[1])
        self.res = []

        self.dfs('JFK')
        print(self.res)
        return self.res[::-1]
    def dfs(self,node):
        while self.adj[node]:
            nei = heapq.heappop(self.adj[node])
            self.dfs(nei)
        self.res.append(node)
        
            




            

        