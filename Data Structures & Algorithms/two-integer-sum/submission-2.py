class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in d:
                return [d[remain],i]
            d[num] = i
        