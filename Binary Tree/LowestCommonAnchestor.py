# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Super inefficient solution but easy to understand
        Algo: get the path till the nodes. From the resultant 2 lists, whenever any element does not match, return the
        previous element
        """
        path, result = [], []
        if not root:
            return None
        else:
            self.getPath(root, p, q, path, result)

        pPath, qPath = result[0], result[1]
        i = 0

        minLen = min(len(pPath), len(qPath))

        while i < minLen:
            if pPath[i].val != qPath[i].val:
                return pPath[i - 1]
            i += 1

        return pPath[i - 1]

    def getPath(self, root, p, q, path, result):
        if root:
            path = path + [root]

            if root == p or root == q:
                result.append(path)

            self.getPath(root.left, p, q, path, result)
            self.getPath(root.right, p, q, path, result)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time complexity is O(n), space complexity O(h)
        """
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # at leaf nodes, left and right both are null, it will return right(in this code), which is null
        # if left is null, go for right node result
        # if right is null go for left node result
        if not left:
            return right
        if not right:
            return left
        # so when left and right both have values, it will return root
        return root