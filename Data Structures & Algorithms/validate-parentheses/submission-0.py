class Solution:
    def isValid(self, s: str) -> bool:
        d = {}
        d[')'] = '('
        d[']'] = '['
        d['}'] = '{'
        ans = []

        for i in s:
            ans.append(i)
            if len(ans)>1 and i in d:
                if ans[-2] == d[i]:
                    ans.pop()
                    ans.pop()
        return True if ans == [] else False



        
        