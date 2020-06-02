# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        else:
            return self.getBST(nums, 0, len(nums) - 1)

    def getBST(self, nums, start, end):
        mid = start + (end - start) // 2

        if start <= end:
            root = TreeNode(nums[mid])
            root.left = self.getBST(nums, start, mid - 1)
            root.right = self.getBST(nums, mid + 1, end)
            return root
        else:
            return None


def printTree(root):
    if root:
        print (root.val)
        printTree(root.left)
        printTree((root.right))


solution = Solution()
nums = [30, 32, 34, 35, 37, 40, 45]
printTree(solution.sortedArrayToBST(nums))