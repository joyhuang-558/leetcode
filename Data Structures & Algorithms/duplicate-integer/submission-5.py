class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set(nums)
        if len(nums)>len(uniq):
            return True
        return False
        