
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = math.ceil(sum(piles)/h)
        r = max(piles)

        for k in range(l,r+1):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/k)
            
            if total_time<=h:
                return k
        
        