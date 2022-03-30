# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def isBadVersion(self, n):
        # This is added to eliminate error, otherwise this problem is from Leetcode
        if n < 3:
            return False
        else:
            return True

    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            if self.isBadVersion(n):
                return 1

        return self.findFirstBadVersion(0, n)

    def findFirstBadVersion(self, start, end):
        mid = start + (end - start) // 2

        while start < end:
            # if the mid is bad and mid-1 is not bad, then it's the first bad version, otherwise binary search
            # mid > 0 condition is added for n = 2, mid is 0th index -> 1, it will throw array out of bounds
            if mid > 0 and self.isBadVersion(mid - 1) == False and self.isBadVersion(mid) == True:
                return mid
            else:
                if self.isBadVersion(mid) == False:
                    return self.findFirstBadVersion(mid + 1, end)
                else:
                    return self.findFirstBadVersion(start, mid - 1)

        return start
