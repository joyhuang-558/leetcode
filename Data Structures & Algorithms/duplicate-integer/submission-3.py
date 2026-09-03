class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = []
        for i in nums:
            if i not in uniq:
                uniq.append(i)
            else: 
                return True
        return False
        