# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            self.findSum(root)
        return self.total

    def findSum(self, root):
        if root:
            if root.left and not root.left.left and not root.left.right:
                self.total += root.left.val
            self.findSum(root.left)
            self.findSum(root.right)