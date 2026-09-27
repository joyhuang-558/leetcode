class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def backtrack(left,right):

            if left==0 and right ==0:
                print("".join(path.copy()))
                result.append("".join(path.copy()))
                
                return
            
            #left
            if left>0:
                print()
                path.append("(")
                backtrack(left-1,right)  
                path.pop()   
            
            if right>0 and right>left:
                path.append(")")
                backtrack(left,right-1)
                path.pop()
            
        backtrack(n,n)
        return result