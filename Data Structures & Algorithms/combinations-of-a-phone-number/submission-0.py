class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        track = []
        self.digits = digits
        self.backtrack(0,track)
        return self.res
    def backtrack(self,index,track):
        mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }
        if len(self.digits)==0:
            self.res = []
            return 
        elif index == len(self.digits):
            self.res.append("".join(track.copy()))
            return
        for i in mapping[self.digits[index]]:
            track.append(i)
            self.backtrack(index+1,track)
            track.pop()
        

        