class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        res = 0
        while l<r:
            cur_area = (r-l)*min(heights[l],heights[r])
            res = max(cur_area,res)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
            



        