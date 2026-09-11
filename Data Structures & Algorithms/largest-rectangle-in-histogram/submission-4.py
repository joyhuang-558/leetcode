class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        stack = [] 
        max_res = 0

        for i,h in enumerate(heights):
            if not stack:
                stack.append(i)

            elif h>=heights[stack[-1]]:
                stack.append(i)
            
            else:

                while stack and h<heights[stack[-1]]:
                    pop_height = heights[stack[-1]]
                    stack.pop()

                    if stack:
                        width = i-stack[-1]-1
                    
                    else:
                        width = i
                    

                    res = width*pop_height
                    max_res = max(res,max_res)

                stack.append(i)
                
            
        return max_res


        