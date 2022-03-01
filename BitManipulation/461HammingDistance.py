class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR x and y. It will leave only the bits where corresponding bits are different
        x = x ^ y
        count = 0

        # find number of set bits
        while x != 0:
            if x & 1 == 1:
                count += 1

            x = x >> 1

        return count


solution = Solution()
assert solution.hammingDistance(16, 15) == 5
assert solution.hammingDistance(1, 4) == 2