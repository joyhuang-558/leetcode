class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniq = []
        for i in nums:
            if i not in uniq:
                uniq.append(i)
            else:
                return i

            
        