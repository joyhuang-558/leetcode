class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for i in s:
            if i.isalnum():
                clean.append(i.lower())
        left, right = 0,len(clean)-1
        while left <= right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
            

        