class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        track = []
        candidates.sort()
        self.backtrack(track,candidates,0,target)
        return self.res


    def backtrack(self,track,candidates,start,remain):
        if remain == 0:
            self.res.append(track.copy())
            return
        elif remain < 0:
            return
        else:
            for i in range(start,len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue
                track.append(candidates[i])
                self.backtrack(track,candidates,i+1,remain-candidates[i])
                track.pop()



        