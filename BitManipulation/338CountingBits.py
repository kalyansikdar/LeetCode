from typing import List


class Solution:
    """
    How to count bits: And 1 with a number. So it will check the right most(least significant) bit, if it is set or not.
    If set, increase the count. Then right shift the number by 1.
    TC: Number of bits in N. 
    """
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            result.append(self.countBitsInADigit(i))

        return result

    def countBitsInADigit(self, i):
        count = 0

        while i != 0:
            if i & 1 == 1:
                count += 1

            i = i >> 1

        return count


solution = Solution()
assert solution.countBits(20) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2]
assert solution.countBits(4) == [0,1,1,2,1]