class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in nums:
            if num-1 not in num_set:
                # num is the start
                cur_res = 1
                while num+1 in num_set:
                    cur_res+=1
                    num = num+1
                res = max(res,cur_res)
        return res


            
                

        