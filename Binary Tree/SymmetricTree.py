# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time complexity: O(n) Because we traverse the entire input tree once, the total run time is O(n)
    Space complexity : The number of recursive calls is bound by the height of the tree.
    In the worst case, the tree is linear and the height is in O(n).
    Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val == root2.val:
            return self.checkSymmetry(root1.left, root2.right) and self.checkSymmetry(root2.left, root1.right)
        else:
            return False
