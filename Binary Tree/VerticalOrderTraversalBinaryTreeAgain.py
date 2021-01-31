# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        cache = {}
        result = []
        if not root:
            return []
        else:
            self.fillCache(root, 0, 0, cache)

        minKey = min(cache.keys())
        maxKey = max(cache.keys())

        for i in range(minKey, maxKey + 1):
            # Example cache: {0: [[0, 1], [2, 5], [2, 6]], -1: [[1, 2]], -2: [[2, 4]], 1: [[1, 3]], 2: [[2, 7]]}
            # sorted(cache[i]) with return the values in list format, but then we will have to get only the node values
            cache_val = sorted(cache[i], key=lambda x: (x[0], x[1]))
            result.append([i[1] for i in cache_val])    # getting only the node values

        return result

    def fillCache(self, root, row, col, cache):
        if root:
            if row not in cache:
                # storing col is needed as we need to have the node values sorted.
                cache[row] = [[col, root.val]]
            else:
                cache[row].append([col, root.val])
            # if the root node is (0,0), then the left child is (-1, 1) and right child is (1, 1)
            self.fillCache(root.left, row - 1, col + 1, cache)
            self.fillCache(root.right, row + 1, col + 1, cache)