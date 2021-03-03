from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        numbersMap = {}

        for num in nums:
            numbersMap[num] = 1

        for i in range(n + 1):
            if i not in numbersMap:
                return i

        return -1


solution = Solution()
nums = [3, 0, 1]
assert solution.missingNumber(nums) == 2
nums = [0, 1]
assert solution.missingNumber(nums) == 2
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
assert solution.missingNumber(nums) == 8
nums = [0]
assert solution.missingNumber(nums) == 1
