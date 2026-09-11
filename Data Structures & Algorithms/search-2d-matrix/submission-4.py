class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n-1

        while l<r:
     
            mid = (l+r)//2
            print(f"mid = {mid}")
            mid_i = mid//n
            print(f"mid_i = {mid_i}")
            mid_j = mid%n
            print(f"mid_j = {mid_j}")
            
            mid_num = matrix[mid_i][mid_j]
            print(f"mid_num = {mid_num}")

            if mid_num==target:
                return True
            elif mid_num>target:
                r-=1
            else:
                l+=1
        return False
        
        