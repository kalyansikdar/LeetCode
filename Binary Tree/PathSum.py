# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        path = []
        allPathSums = []

        if not root:
            return None
        else:
            self.findPathSum(root, path, allPathSums)
            for path in allPathSums:
                if sum(path) == targetSum:
                    return True
            return False

    def findPathSum(self, root, path, allPathSums):
        if root:
            path = path + [root.val]
            # at leaf node add the path to the result, otherwise keep on adding the node values
            if not root.left and not root.right:
                allPathSums.append(path)

            self.findPathSum(root.left, path, allPathSums)
            self.findPathSum(root.right, path, allPathSums)

    def hasPathSumII(self, root: TreeNode, targetSum: int) -> bool:
        """
            Time Complexity = O(n), where n is the number of nodes - O(n), visit each node once
            - Space Complexity = O(h), where h is the height of the tree -- ??
            """
        if not root:
            return None
        else:
            return self.isPathSum(root, 0, targetSum)

    def isPathSum(self, root, pathSum, targetSum):
        if not root:
            return False

        pathSum += root.val
        # in case of leaf node, we check if pathSum is equal to targetSum
        if not root.left and not root.right:
            if pathSum == targetSum:
                return True
        # if either one return true, we return true, hence or condition
        return self.isPathSum(root.left, pathSum, targetSum) or self.isPathSum(root.right, pathSum, targetSum)