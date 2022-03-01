import math
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        This is based on Sieve of Eratosthenes
        Time complexity: NloglogN -> memorize it
        """
        count = 0
        tracker = [True] * (n + 1)

        for i in range(2, n):
            if tracker[i] == True:
                count += 1

                for j in range(i * 2, n + 1, i):
                    tracker[j] = False

        return count

    def countPrimes_better(self, n: int) -> int:
        if n < 2:
            return 0

        tracker = [True] * n
        tracker[0] = tracker[1] = False

        for i in range(int(math.sqrt(n)) + 1):
            # we can run till N/2 because one of the every two factors of N will always be greater than N/2
            if tracker[i] == True:

                for j in range(i * 2, n, i):
                    tracker[j] = False

        return sum(tracker)


sol = Solution()
assert sol.countPrimes(2) == 0
assert sol.countPrimes(10) == 4
assert sol.countPrimes_better(2) == 0
assert sol.countPrimes_better(10) == 4