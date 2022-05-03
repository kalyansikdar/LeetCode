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

            # objective is to find greater area, greater height results in greater area
            # hence, we keep the greater height, move the other pointer
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return capacity

    def maxArea_brute_force(self, height: List[int]) -> int:
        """
        Time complexity: O(N^2), This solution will result in TLE
        """
        area = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])

                area = max(area, h * (j - i))

        return area


solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
assert solution.maxArea(height) == 49
height = [4, 3, 2, 1, 4]
assert solution.maxArea(height) == 16
