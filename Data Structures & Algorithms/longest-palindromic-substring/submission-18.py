class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i,a in enumerate(s):
            #print(f"i,a = : {i} {a}")
            odd = cur_ans = self.max_Palindromic(i,i,s)
            even = cur_ans = self.max_Palindromic(i,i+1,s)
            cur_ans = odd if len(odd)>len(even) else even
        
            ans = cur_ans if len(cur_ans)>len(ans) else ans
            #print(f"这一轮更新的ans: {ans}")
        return ans
      
    def max_Palindromic(self,left,right,s):
        while left>=0 and right <=len(s)-1 and s[left]==s[right]:
            left -= 1
            right += 1   
        return s[left+1:right]


        