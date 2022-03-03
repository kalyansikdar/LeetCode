class Solution:
    def isPowerOfTwo_iterative(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 2 == 0:
            n = n // 2

        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        """
        TC: O(1) This operation can be done in constant time
        """
        # base case
        if n == 0 or n == 1:
            return n

        # AND of 2^n (a power of 2) and one less than that number will always be 0
        return n & (n - 1) == 0


solution = Solution()
assert solution.isPowerOfTwo(16) == True
assert solution.isPowerOfTwo(7) == False
