class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range (len(nums)-k):
            cur = heapq.heappop(nums)
        return nums[0]

        