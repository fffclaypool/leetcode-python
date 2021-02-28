class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        pos = 0
        for i in range(len(A)):
            if not A[i] % 2:
                A[pos], A[i] = A[i], A[pos]
                pos += 1
        return A
