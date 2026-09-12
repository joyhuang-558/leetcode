class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid]==target:
                return mid
            
            elif nums[mid]>nums[r]:
                #左边递增
                
                #target 在左边递增的里面
                if nums[l]<=target <nums[mid]:
                    r=mid-1
                else:
                    l = mid+1

            elif nums[mid]<=nums[r]:
                #右边递增
                if nums[mid]<target <=nums[r]:
                    l=mid+1
                else:
                    r = mid-1
        
        return -1


        