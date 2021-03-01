class Solution:
    def isHappy(self, n: int) -> bool:

        seen = {}
        return self.calcHappy(n, seen)

    def calcHappy(self, n, seen):

        sum_n = 0
        for v in str(n):
            sum_n += int(v) ** 2

        if sum_n == 1:
            return True
        elif sum_n in seen:
            return False
        else:
            seen[sum_n] = True
            return self.calcHappy(sum_n, seen)
