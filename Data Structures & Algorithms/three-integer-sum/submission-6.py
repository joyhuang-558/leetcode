class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            if num>0:
                break
            if i>1 and nums[i-1]==num:
                continue
            target = -num
            l,r = i+1,len(nums)-1
            rest = nums[l]+nums[r]
            if rest>0:
                r-=1
            elif rest<0:
                l+=1
            else:
                res.append([i,l,r])
                l+=1
                while l<r and nums[l]==num[l-1]:
                    l+=1
        return res



        