class Solution:
    def isValid(self, s: str) -> bool:
        map = {}
        map[')'] = '('
        map[']'] = '['
        map['}'] = '{'
        stack = []
        for i in s:
            if i in map:
                if stack:
                    cur = stack.pop()
                    if map[i]==cur:
                        continue
                    return False
                else: return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else: return False

                

        
        