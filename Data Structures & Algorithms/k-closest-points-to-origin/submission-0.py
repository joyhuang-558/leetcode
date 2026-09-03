import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x = p[0]
            y = p[1]
            heap.append((x*x+y*y,x,y))
        heapq.heapify(heap)

        ans = []

        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            ans.append([x,y])
        
        return ans
            
        