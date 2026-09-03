class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        track = []
        self.backtrack(nums,track,0,target)
        return self.res
    def backtrack(self,nums,track,start,remain):
        if remain == 0:
            self.res.append(track.copy())
            return
        elif remain < 0:
            return
        else:
            for i in range(start,len(nums)):
                track.append(nums[i])
                self.backtrack(nums,track,i,remain-nums[i])

                track.pop()

            


        