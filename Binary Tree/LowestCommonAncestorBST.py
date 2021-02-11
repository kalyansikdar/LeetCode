# Definition for a binary tree node.
from binarytree import build


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root


arr = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
t1 = build(arr)
print(t1)
solution = Solution()
# assert solution.lowestCommonAncestor(t1, TreeNode(2), TreeNode(4)) == Node with val 2
