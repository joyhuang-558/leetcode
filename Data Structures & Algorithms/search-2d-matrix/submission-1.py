class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n-1

        for i in range(m):
            for j in range(n):
                mid = (l+r)//2

                mid_i = mid//n
                mid_j = mid%n
                
                mid_num = matrix[mid_i][mid_j]

                if mid_num==target:
                    return True
                elif mid_num>target:
                    r-=1
                else:
                    l-=1
        return False
        
        