class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        def max_rec(i):
            h = heights[i]
            l=i
            r=i

            while l>=0 and heights[l]>=h:
                l-=1
            res_l = l+1
            
            while r<=len(heights)-1 and heights[r]>=h:
                r+=1
            res_r = r-1

            res = h*(res_r-res_l+1)

            return res
        
        max_res = 0
        for i in range(len(heights)):
            max_res = max(max_res,max_rec(i))
        
        return max_res

        