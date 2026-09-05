class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        res = []
        for i in range(k):
            heapq.heappush(h,(-nums[i],i))
        
        
        res.append(-h[0][0])


        for i in range(k,len(nums)):
            heapq.heappush(h,(-nums[i],i))
           

          
            while h[0][1]<i-k+1:
                heapq.heappop(h)
            
            cur_max = h[0][0]
            
            res.append(-cur_max)
        
        return res
                
            

            



        