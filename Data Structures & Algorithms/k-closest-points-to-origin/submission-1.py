class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for p in points:
            d = p[0]**2+p[1]**2
            dis.append([d,[p[0],p[1]]])
        heapq.heapify(dis)
        res = []
        for i in range(k):
            cur = heapq.heappop(dis)
            res.append(cur[1])
        return res
        
        