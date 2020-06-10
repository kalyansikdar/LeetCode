# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, L: int, R: int) -> int:
        if not root:
            return 0

        applicableNodes = []
        self.getNodes(root, L, R, applicableNodes)
        print(applicableNodes)
        return sum(applicableNodes)

    def getNodes(self, root, L, R, result):
        if root:
            if L <= root.val <= R:
                result.append(root.val)
            self.getNodes(root.left, L, R, result)
            self.getNodes(root.right, L, R, result)
        else:
            return