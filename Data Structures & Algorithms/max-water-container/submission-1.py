class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        ans = 0
        
        while i < j:
            lenth = j-i
            cur_area = lenth*min(heights[i],heights[j])
            ans = max(ans,cur_area)

            if heights[i] <= heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
        return ans

            

 


        
        