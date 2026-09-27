class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path

        def backtrack(left,right):

            if left==0 and right ==0:
                result.append(path.copy())
                return
            
            #left
            if left>0:
                path.append("(")
                backtrack(left-1,right)     
            
            if right>0 and right>left:
                path.append(")")
                backtrack(left,right-1)
            
        backtrack(n,n)
        return result