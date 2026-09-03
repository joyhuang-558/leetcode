class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for p in range(len(intervals)):
            if newInterval[1]<intervals[p][0]:
                res.append(newInterval)
                return res+intervals[p:]
            elif newInterval[0]>intervals[p][1]:
                res.append(intervals[p])
            else:
                cur_start = min(newInterval[0],intervals[p][0])
                cur_end = max(newInterval[1],intervals[p][1])
                newInterval = [cur_start,cur_end]
        res.append(newInterval)
        return res
        

        