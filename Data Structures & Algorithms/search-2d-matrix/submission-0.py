class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m*n-1
        while left <= right:
            mid = (left+right)//2
            num = matrix[mid//n][mid%n]

            if num == target:
                return True
            elif num>target:
                right -= 1
            else: 
                left += 1
        return False

        