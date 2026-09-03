class Solution:
    def isValid(self, s: str) -> bool:
        map = {}
        map[')'] = '('
        map[']'] = '['
        map['}'] = '{'
        stack = []
        for i in s:
            if i in map:
                if not stack or map[i]!=stack.pop():
                    return False
            else:
                stack.append(i)
        return not stack


                

        
        