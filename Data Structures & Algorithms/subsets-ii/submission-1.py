class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        track = []
        nums.sort()
        self.backtrack(nums,track,0)
        return self.res

    def backtrack(self,nums,track,start):
        self.res.append(track.copy())
        for i in range(start,len(nums)):
            if i > start and nums[i]==nums[i-1]:
                continue
            track.append(nums[i])
            self.backtrack(nums,track,i+1)
            track.pop()
