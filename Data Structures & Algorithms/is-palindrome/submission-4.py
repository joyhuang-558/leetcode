class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            if not s[l].isalpha():
                l+=1
            if not s[r].isalpha():
                r-=1
            elif s[l].lower()!=s[r].lower():
                print(s[l])
                print(s[r])
                return False
            else:
                l+=1
                r-=1
        return True

        