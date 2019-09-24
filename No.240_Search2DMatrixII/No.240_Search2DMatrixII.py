class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix) and len(matrix[0])
        i, j = 0, col-1
        
        while i < row and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False