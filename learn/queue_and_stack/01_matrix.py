class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    top = matrix[i-1][j] if i else float('inf')
                    left = matrix[i][j-1] if j else float('inf')
                    matrix[i][j] = min(top, left) + 1
        for k in reversed(range(m)):
            for l in reversed(range(n)):
                if cell := matrix[k][l]:
                    bottom = matrix[k+1][l] if k < m-1 else float('inf')
                    right = matrix[k][l+1] if l < n-1 else float('inf')
                    matrix[k][l] = min(cell, bottom + 1, right + 1)
        return matrix
