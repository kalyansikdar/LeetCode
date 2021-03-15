# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            temp = TreeNode(v)
            temp.left = root
            return temp

        else:
            self.addRowAtDepth(root, v, d, 1)

        return root

    def addRowAtDepth(self, root, v, d, currentDepth):
        if root:
            if currentDepth == d - 1:
                left = root.left
                right = root.right

                forLeft = TreeNode(v)
                forLeft.left = left
                forRight = TreeNode(v)
                forRight.right = right

                root.left = forLeft
                root.right = forRight

            self.addRowAtDepth(root.left, v, d, currentDepth + 1)
            self.addRowAtDepth(root.right, v, d, currentDepth + 1)