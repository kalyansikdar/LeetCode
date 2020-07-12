# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxWidth = 1

    def widthOfBinaryTree(self, root) -> int:
        holder = []
        if not root:
            return 0
        else:
            self.fillLevelNodes(root, holder, 1, 0)
        return self.maxWidth

    def fillLevelNodes(self, root, holder, index, depth):
        if root:
            if len(holder) == depth:
                holder.append(index)        # for leftmost node in every level, it adds the index
            else:
                self.maxWidth = max(self.maxWidth, index - holder[depth] + 1)   # width is calculated for every node
                # afterwards and max value is set

            self.fillLevelNodes(root.left, holder, 2 * index, depth + 1)
            self.fillLevelNodes(root.right, holder, 2 * index + 1, depth + 1)
