class Solution:
    def isValid(self, s: str) -> bool:
        map_dic = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        q = []
        #如果右括号，不要加进去，pop最后一个出来match
        #如果左括号，直接加进去
        for a in s:
            
            if a not in map_dic:
                
                q.append(a)

            else:
 
                if len(q)==0:
                    return False
                cur = q.pop()

                if map_dic[a]!=cur:

                    return False

        return True


        