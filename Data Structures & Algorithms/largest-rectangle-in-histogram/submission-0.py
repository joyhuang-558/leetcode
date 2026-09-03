class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = []
        stack = []
        for i,h in enumerate(heights):
            if len(stack)==0:
                stack.append((i,h))
            elif h>=stack[-1][-1]:
                stack.append((i,h))
            else:
                while stack and h<stack[-1][-1]:
                    index,height = stack.pop()
                    ans.append((i-index)*height)
                start = index
                stack.append((start,h))
        for i,h in stack:
            ans.append((len(heights)-i)*h)
        return max(ans)


            

