class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        return True
nums=[1,2,3,3]       
sol = Solution()
print(sol.hasDuplicate(nums))