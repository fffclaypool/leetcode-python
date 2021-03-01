class Solution:
    def searchMatrix(self, matrix, target):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        height, width = len(matrix), len(matrix[0])
        row, col = height-1, 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True

        return False
