# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result
        else:
            self.getZigzagOrder(root, 0, result)
        return result

    def getZigzagOrder(self, root, depth, result):
        if root:
            if depth == len(result):
                result.append([])

            if depth % 2 == 0:
                result[depth].append(root.val)      # if level is divisible by 2, append the value
            else:
                result[depth].insert(0, root.val)   # if level is not divisible by 2, insert the value at index 0
            self.getZigzagOrder(root.left, depth + 1, result)
            self.getZigzagOrder(root.right, depth + 1, result)