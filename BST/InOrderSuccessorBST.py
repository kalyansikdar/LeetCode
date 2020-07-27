# Given a binary search tree and a node in it, find the in-order successor of that node in the BST. The successor of
# a node p is the node with the smallest key greater than p.val. Example 1: Input: root = [2, 1, 3], p = 1 Output: 2
# Explanation: 1 's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
#
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
#
# Note:
# If the given node has no in-order successor in the tree, return null.
# It's guaranteed that the values of the tree are unique.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)

            if left:
                return left
            else:
                return root

    def inorderSuccessor_iterative(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

    def inorderSuccessor_iterative_detailed(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        parent = None

        while root.val != p.val:
            if p.val < root.val:
                parent = root
                root = root.left
            elif p.val > root.val:
                root = root.right

        if root.right:
            return self.getLeftMost(root.right)
        else:
            return parent

    def getLeftMost(self, root):
        while root.left:
            root = root.left

        return root