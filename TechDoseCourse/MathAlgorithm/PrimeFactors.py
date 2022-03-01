# Q: List all prime factors of N
# Ex: 20 = 2*2*5
# Ex: 60 = 2*2*3*5
import math


class Solution:
    def getPrimeFactors(self, n):
        result = []

        for i in range(2, int(math.sqrt(n))+1):
            # reduce n till it's divisible by any number
            while n % i == 0:
                n = int(n/i)
                result.append(i)

        if n > 1:
            result.append(n)

        return result


sol = Solution()
print(sol.getPrimeFactors(21))
print(sol.getPrimeFactors(34))
