class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = []
        for i,a in enumerate(s):
            #print(f"i:{i}")
            self.total_p(s,i,i)
            #print(f"1:{self.ans}")
            self.total_p(s,i,i+1)
            #print(f"1:{self.ans}")
        return len(self.ans)

    def total_p(self,s,left,right):
        while left>=0 and right<=len(s)-1:
            if s[left]==s[right]:
                #print(f"left,right:{s[left]}{s[right]}")
                self.ans.append(s[left:right+1])
                left-=1
                right+=1
            else:
                break



        