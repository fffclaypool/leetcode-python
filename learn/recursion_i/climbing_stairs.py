class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        else:
            primes = [True] * n
            primes[0] = primes[1] = False
            for num in range(2, n):
                if primes[num]:
                    primes[2*num:n:num] = [False]*((n-1)//num-1)
            return sum(primes)
