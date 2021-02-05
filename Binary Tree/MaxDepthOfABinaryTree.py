# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.depth = 1

    def maxDepth(self, root: TreeNode) -> int:
        # in this method we are doing top-down recursion
        if not root:
            return 0
        else:
            self.findMaxDepth(root, 1)  # Depth starts at 1
            return self.depth

    def findMaxDepth(self, root, localDepth):
        # at leaf node, update the depth to a GLOBAL variable
        if not root.left and not root.right:
            self.depth = max(self.depth, localDepth)

        if root.left:
            self.findMaxDepth(root.left, localDepth + 1)

        if root.right:
            self.findMaxDepth(root.right, localDepth + 1)

        return
