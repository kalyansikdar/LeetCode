# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        else:
            if val > root.val:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.left = self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST_iterative(self, root: TreeNode, val: int) -> TreeNode:
            if not root:
                return TreeNode(val)

            curr = root
            queue = [curr]

            while curr:
                if curr.left and val < curr.val:
                    curr = curr.left

                elif curr.right and val > curr.val:
                    curr = curr.right
                else:
                    break

            newNode = TreeNode(val)
            if val > curr.val:
                curr.right = newNode
            else:
                curr.left = newNode

            return root