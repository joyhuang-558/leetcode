class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,num in enumerate(nums):
            if num>0:
                break
            if i>=1 and nums[i-1]==num:
                continue

            target = -num
            l,r = i+1,len(nums)-1

            while l<r:
                rest = nums[l]+nums[r]
                if rest>target:
                    r-=1
                elif rest<target:
                    l+=1
                else:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1

                    while (l<r and nums[l]==nums[l-1]):
                        l+=1
        return res



        