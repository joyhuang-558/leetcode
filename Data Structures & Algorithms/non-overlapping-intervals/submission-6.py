class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:-i[0])
        start = float('inf')
        count = 0
        for i in intervals:
            if i[1] <= start:
                count += 1
                start = i[0]
        return len(intervals)-count


        