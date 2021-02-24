class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # divide n by 3 and check if reminder is 0, if not return False, else next iteration
        if n <= 0:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n = n / 3

        return True


solution = Solution()
assert solution.isPowerOfThree(27) == True
assert solution.isPowerOfThree(45) == False
assert solution.isPowerOfThree(-9) == False
