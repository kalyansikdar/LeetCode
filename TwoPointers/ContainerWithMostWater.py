import sys
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time complexity O(n) as it's one pass
        capacity of container would be difference between two walls and it's width.
        Start with two pointers and keep finding the capacity while you come to middle
        """
        capacity = - sys.maxsize
        start = 0
        end = len(height) - 1

        while start < end:
            width = end - start
            capacity = max(capacity, min(height[start], height[end]) * width)

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return capacity


solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
assert solution.maxArea(height) == 49
height = [4,3,2,1,4]
assert solution.maxArea(height) == 16