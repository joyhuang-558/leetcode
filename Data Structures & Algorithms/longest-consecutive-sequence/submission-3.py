class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if (num-1) not in num_set:
                lenth = 1
                while (num+lenth) in num_set:
                    lenth += 1
                res = max(res,lenth)
        return res


        