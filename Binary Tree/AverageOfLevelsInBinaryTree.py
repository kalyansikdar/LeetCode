# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levelWiseGroup = []
        if not root:
            return levelWiseGroup
        else:
            self.formLevelWiseGroup(root, levelWiseGroup, 0)

        return [sum(i) / len(i) for i in levelWiseGroup]

    def formLevelWiseGroup(self, root, levelWiseGroup, depth):
        if root:
            if depth == len(levelWiseGroup):
                levelWiseGroup.append([root.val])
            else:
                levelWiseGroup[depth].append(root.val)

            self.formLevelWiseGroup(root.left, levelWiseGroup, depth + 1)
            self.formLevelWiseGroup(root.right, levelWiseGroup, depth + 1)