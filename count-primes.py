import math


class Solution:
    def countPrimes(self, n: int) -> int:
        # the Eratosthenes method
        # O(nloglogn)
        isPrimes = [True for _ in range(n-1)]
        for p in range(2, int(math.sqrt(n)) + 1):
            if not isPrimes[p-1]: continue
            i = p
            while p * i <= n-1:
                isPrimes[p * i - 1] = False
                i += 1
        return max(0, sum(isPrimes) - 1)
    ## for each number check whether it's a prime and add it to res
    # time limit error
    # def countPrimes2(self, n: int) -> int:
    #     c = 0
    #     for i in range(2,n):
    #         if self.isPrime(i):
    #             c += 1
    #     return c
    #
    #
    # def isPrime(self,n):
    #     i = 2
    #     while i * i <= n:
    #         if n % i == 0:
    #             return False
    #         i += 1
    #     return True

n = 10
print(Solution().countPrimes(n))