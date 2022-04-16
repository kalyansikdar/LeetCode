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
        Time complexity: O(N): Traversing each node once
        Space complexity: O(logn/h) for recursion call stack
        """
        # base case
        if not root:
            return None
        # if the node is either p or q, return p or q
        # This has to be the first condition, else if leaf node is p or q, it won't be captured
        if root == p or root == q:
            return root

        # go left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both left and right subtrees holds either nodes, root is the common ancestor
        if left and right:
            return root

        # if either is found on left and right, return the found side
        if left or right:
            return left or right