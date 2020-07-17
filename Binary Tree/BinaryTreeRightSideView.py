# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        result = []
        if not root:
            return []
        else:
            self.findRightSideView(root, 0, result)
        return result

    def findRightSideView(self, root, depth, result):
        if root:
            if len(result) == depth:  # only add if that element is last in that level
                result.append(root.val)

            if root.right:
                self.findRightSideView(root.right, depth + 1, result)
            if root.left:
                self.findRightSideView(root.left, depth + 1, result)
