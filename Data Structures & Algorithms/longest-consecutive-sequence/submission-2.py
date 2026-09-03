# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         num_set = set(nums)
#         res = 0
#         for num in num_set:
#             if (num-1) not in num_set:
#                 lenth = 1
#                 while (num+lenth) in num_set:
#                     lenth += 1
#             res = max(res,lenth)
#         return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        