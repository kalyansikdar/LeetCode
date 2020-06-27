# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        holder = []
        if not root:
            return 0
        else:
            self.getSum(root, holder, 0, "")
        return sum([int(i) for i in holder])

    def getSum(self, root, holder, depth, sumVal):
        if root:
            if depth == 0:
                sumVal = ""

            sumVal += str(root.val)
            if not root.left and not root.right:
                holder.append(sumVal)
                return
            else:
                self.getSum(root.left, holder, depth + 1, sumVal)
                self.getSum(root.right, holder, depth + 1, sumVal)
        else:
            return