# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        result = []
        depth = 0
        if not root:
            return []
        else:
            self._levelOrderBottom(root, depth, result)
        return result[::-1]

    def _levelOrderBottom(self, root, depth, result):
        if root:
            if len(result) == depth:
                result.append([])
            result[depth].append(root.val)
            self._levelOrderBottom(root.left, depth + 1, result)
            self._levelOrderBottom(root.right, depth + 1, result)
        else:
            return
