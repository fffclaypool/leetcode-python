class Solution:
    def replaceElements(self, A, mx=-1):
        for i in range(len(A) - 1, -1, -1):
            A[i], mx = mx, max(mx, A[i])
        return A
