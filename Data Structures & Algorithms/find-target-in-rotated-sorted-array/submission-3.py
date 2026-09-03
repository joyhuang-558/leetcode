class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right+left)//2
            print(f"mid = {mid}")
            if nums[mid]==target:
                return mid
            #如果左边有序
            elif nums[mid]>=nums[left]:
                print(f"nums[mid] = {nums[mid]}")
                print('左边有序')
                if nums[left]<=target<nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
                print(f"left = {left}")
            else:
                #如果右边有序
                print('右边有序')
                if nums[mid]<target<=nums[right]:
                    left = mid +1
                else:
                    right = mid -1
        return -1





        