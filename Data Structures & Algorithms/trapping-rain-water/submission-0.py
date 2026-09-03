class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_l = max_r = 0
        res = 0
        while left <= right:
            if height[left]<height[right]:
                if height[left]>max_l:
                    max_l = height[left]
                else:
                    water = max_l-height[left]
                    res+= water
                left += 1
            elif height[left]>=height[right]:
                if height[right]>max_r:
                    max_r = height[right]
                else:
                    water = max_r-height[right]
                    res+= water
                right -= 1
        return res




        