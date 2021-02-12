# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            return self._getBST(nums, 0, len(nums) - 1)

    def _getBST(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        root = TreeNode(nums[mid])
        root.left = self._getBST(nums, start, mid - 1)
        root.right = self._getBST(nums, mid + 1, end)

        return root