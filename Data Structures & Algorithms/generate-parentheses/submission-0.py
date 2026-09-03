class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        track = []
        self.backtrack(track,0,0,n)
        return self.res
    def backtrack(self,track,left,right,n):
        if len(track)==2*n:
            self.res.append("".join(track.copy()))
            return
        else:
            if left<n:
                track.append("(")
                self.backtrack(track,left+1,right,n)
                track.pop()
            if right<left:
                track.append(")")
                self.backtrack(track,left,right+1,n)
                track.pop()
            

        