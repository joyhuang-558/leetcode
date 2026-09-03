class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ls = []
        for i in range(len(nums)-2):
            #如果和前一个一样，跳过
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #如果和后两个加起来大于0，结束
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    ls.append([nums[i],nums[j],nums[k]])

                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else: k -= 1
       
        return ls


        