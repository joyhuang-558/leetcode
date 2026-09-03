class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.res = []
        self.track = []
        self.backtrack(0)
        return self.res
    
    def isPalindrome(self,left,right):
        while left<=right:
            if self.s[left]!= self.s[right]:
                return False
            left+=1
            right-=1
        return True
    def backtrack(self,start):
        if start == len(self.s):
            self.res.append(self.track.copy())
            return
        for end in range(start,len(self.s)):
            if not self.isPalindrome(start,end):
                continue
            else:
                self.track.append(self.s[start:end+1])
            self.backtrack(end+1)
            self.track.pop()
        