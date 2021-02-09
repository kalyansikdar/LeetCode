# Helper function to find minimum value node in a given BST
from collections import deque
from binarytree import build


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrderSuccessor(self, root, p):
        if not root:
            return None
        curr = root
        prev = None

        while curr:
            if curr.val > p.val:
                prev = curr
                curr = curr.left
            else:
                curr = curr.right

        return prev

    def inorder_recursive(self, root, p):
        return self.inOrderSuccessor_recursive(root, p, None)

    def inOrderSuccessor_recursive(self, root, p, successor):
        if not root:
            return None

        if root.val == p.val:
            if root.right:
                return self.findMinVal(root.right)
            else:
                return successor

        if root.val > p.val:
            return self.inOrderSuccessor_recursive(root.left, p, root)
        else:
            return self.inOrderSuccessor_recursive(root.right, p, successor)

    def findMinVal(self, root):
        curr = root
        while curr:
            curr = curr.left
        return curr


arr = [5, 3, 6, 2, 4, None, None, 1]
t1 = build(arr)
print(t1)
solution = Solution()
assert solution.inOrderSuccessor(t1, TreeNode(5)).val == 6
assert solution.inOrderSuccessor(t1, TreeNode(6)) is None
assert solution.inOrderSuccessor(t1, TreeNode(2)).val == 3
assert solution.inOrderSuccessor(t1, TreeNode(3)).val == 4
assert solution.inorder_recursive(t1, TreeNode(5)).val == 6
assert solution.inorder_recursive(t1, TreeNode(6)) is None
assert solution.inorder_recursive(t1, TreeNode(2)).val == 3
assert solution.inorder_recursive(t1, TreeNode(3)).val == 4