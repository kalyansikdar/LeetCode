# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guess(self, n):
        # It's a dummy function taken
        return None

    def guessNumber(self, n: int) -> int:
        return self.binarySearch(n, 0, n)

    def binarySearch(self, n, start, end):
        mid = (start + end) // 2

        while start <= end:
            if self.guess(mid) == 0:
                return mid

            elif self.guess(mid) == -1:
                return self.binarySearch(n, start, mid - 1)

            else:
                return self.binarySearch(n, mid + 1, end)

        return -1
