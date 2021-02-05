# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        else:
            return self.trim(root, low, high)

    def trim(self, root, low, high):
        if not root:
            return

        if root.val > high:
            return self.trim(root.left, low, high)
        elif root.val < low:
            return self.trim(root.right, low, high)
        else:
            # at this step node becomes left or right of root
            root.left = self.trim(root.left, low, high)
            root.right = self.trim(root.right, low, high)

        return root
