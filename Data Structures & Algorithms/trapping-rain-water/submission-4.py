class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)-1):
            left_max = 0
            right_max = 0
            l = i-1
            r = i+1
            while l>=0 or r<=len(height)-1:
                if l>=0:
                    left_max = max(height[l],left_max)
                    l-=1
                if r<=len(height)-1:
                    right_max = max(height[r],right_max)
                    r+=1
            head = max(min(left_max,right_max)-height[i],0)
            res+=head
        return res
        


 
        