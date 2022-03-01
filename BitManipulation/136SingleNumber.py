from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            result = result ^ i

        return result


solution = Solution()
assert solution.singleNumber([2, 2, 1]) == 1
assert solution.singleNumber([4, 1, 2, 1, 2]) == 4