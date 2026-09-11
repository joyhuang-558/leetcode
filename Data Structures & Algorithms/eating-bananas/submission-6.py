
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles)/h)
        r = max(piles)


        while l<=r:
            k = (l+r)//2


            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/k)
            
            if total_time<=h:
                r = k-1
            else:
                l = k+1
        return l
                
        
        