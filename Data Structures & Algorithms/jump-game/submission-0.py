class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dis = 0
        cur_dis = 0
        for index,num in enumerate(nums):
            if max_dis < index:
                return False

            cur_dis = index+num
            max_dis = max(max_dis,cur_dis)
        return True


        