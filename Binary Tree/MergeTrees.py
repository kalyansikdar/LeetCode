# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        TC: O(N) where N is number if nodes because it's traversing all the nodes
        SC: O(1) as it's not using any extra space, it's updating the first tree itself
        """
        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)

        if root1 or root2:
            return root1 or root2

    def mergeTrees_extra_space(self, t1, t2):
        """
        TC: O(N) where N is number if nodes because it's traversing all the nodes
        SC: O(N) as it's creating a new tree
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2