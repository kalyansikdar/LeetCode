# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.leftBoundary, self.rightBoundary = 0, 0

    def verticalTraversal(self, root: TreeNode) :
        result = []
        cache = {}
        if not root:
            return result

        self.dfs(root, cache, 0, 0)

        for i in range(self.leftBoundary, self.rightBoundary + 1):
            col = sorted(cache[i], key=lambda x: (x[0], x[1]))      # sort the values based on row value (first
            # element) and then the root value itself (second element)
            print (col)
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])     # adding the second element - root value
            result.append(col_sorted)

        return result

    def dfs(self, root, cache, row, col):
        if root:
            if col not in cache:
                cache[col] = [[row, root.val]]
            else:
                cache[col].append([row, root.val])

            # capture left and right column boundary
            self.leftBoundary = min(self.leftBoundary, col)
            self.rightBoundary = max(self.rightBoundary, col)

            self.dfs(root.left, cache, row + 1, col - 1)    # if we go left, column value decreases
            self.dfs(root.right, cache, row + 1, col + 1)   # if we go right, column value increases but row value
            # increases in both cases


