class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniq = set()
        for i in nums:
            if i not in uniq:
                uniq.add(i)
            else:
                return i
        