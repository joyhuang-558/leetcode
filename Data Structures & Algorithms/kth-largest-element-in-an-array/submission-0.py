import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            h.append(-i)
        heapq.heapify(h)
        for i in range(k-1):
            heapq.heappop(h)
        return -h[0]
        


        