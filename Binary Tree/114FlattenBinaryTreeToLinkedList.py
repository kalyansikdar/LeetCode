# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        # at first node, prev is None but thereafter it's the last node processed
        root.right = self.prev
        root.left = None
        # Need the prev to be a global variable to be able to pass the updated value to each recursion calls
        self.prev = root

    def flatten_iterative(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [root]

        if not root:
            return []

        while stack:
            curr = stack.pop()

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)

            if stack:
                # as left node is inserted later, left node will be at the top
                # left node is set to right
                curr.right = stack[-1]

            curr.left = None