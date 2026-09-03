class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        zero_index = []
        non_zero_prod = 1

        for i,num in enumerate(nums):
            if num==0:
                zero_index.append(i)
                continue
            non_zero_prod = non_zero_prod*num
        if len(zero_index)>1:
            return res
        if len(zero_index)==1:
            res[zero_index[0]]=non_zero_prod
            return res
        else:
            for i in range(len(res)):
                res[i]=non_zero_prod//nums[i]
        return res


        
        

        