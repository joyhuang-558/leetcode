import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-s)
        heapq.heapify(heap)
        while len(heap)>=2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,-(y-x))
        return -heap[0] if heap else 0



        



        