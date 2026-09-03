class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i,num in enumerate(nums):
            if far < i:
                return False
            elif far >= i:
                far = max(far,num+i)



        return True




        