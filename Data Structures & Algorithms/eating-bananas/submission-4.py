from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #left是最小速度，right是最大速度，题目要求最小速度
        left = ceil(sum(piles) / h)
        right = max(piles)

        while left <= right:
            mid = (left+right)//2
            time = 0
            for i in piles:
                time += ceil(i/mid)
 
            if time > h:
                #吃不完，太慢
                left = mid + 1
            else:
                right = mid -1
        
        return left
        