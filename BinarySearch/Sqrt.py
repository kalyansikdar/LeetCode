class Solution:
    def mySqrt(self, x: int) -> int:
        # TC: logN because binary search is applied
        if x <= 1:
            return x
        else:
            return self.findSqrt(x, 1, x)

    def findSqrt(self, x, start, end):
        mid = (start + end) // 2

        while start <= end:
            if mid * mid == x:
                return mid

            if mid * mid > x:
                return self.findSqrt(x, start, mid - 1)

            if mid * mid < x:
                return self.findSqrt(x, mid + 1, end)

        # check for 10, at last 4 is the mid and 16 > 10. So findSqrt(x, 4, 3) is called. While loop does not satisfy
        # so mid is returned.
        return mid


solution = Solution()
assert solution.mySqrt(10) == 3
assert solution.mySqrt(17) == 4
assert solution.mySqrt(25) == 5
