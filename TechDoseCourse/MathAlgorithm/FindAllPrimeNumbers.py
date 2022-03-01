# Find all prime numbers from 1 to N
import math


class Solution:
    def findAllPrimes(self, n):
        result = []

        for i in range(2, n):
            if self.isPrime_better(i):
                result.append(i)

        return result

    def isPrime(self, n):
        for i in range(2, n//2):
            if n % i == 0:
                return False

        return True

    def isPrime_better(self, n):
        print(n, math.floor(math.sqrt(n)))
        for i in range(2, (math.sqrt(n))):
            if n % i == 0:
                return False

        return True

    def findAllPrimes_sieveOfEratosthenes(self, n):
        primes = []
        tracker = [True] * (n + 1)

        for i in range(2, n):
            if tracker[i] == True:
                primes.append(i)

                for j in range(i * 2, n + 1, i):
                    tracker[j] = False

        return primes


sol = Solution()
print(sol.findAllPrimes_sieveOfEratosthenes(100))
