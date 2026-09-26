import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       
        heap =[(-count,task) for task,count in Counter(tasks).items()]
        heapq.heapify(heap)

        cool = deque()
        time = 0

        while cool or heap:
            time+=1
            if cool and cool[0][0]<=time:
                task_time,remain,task = cool.popleft()
                heapq.heappush(heap,(remain,task))
            if heap:
                remain,task = heapq.heappop(heap)
                #执行
                remain+=1

                if remain<0:
                    cool.append((time+n+1,remain,task))


        return time
                

                
        
        

        