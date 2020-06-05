# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # above conditions are to find the node
        else:  # once the node is found, if there is not left node, right node becomes the root after root is deleted.
            if not root.left:
                return root.right
            if not root.right:  # if there is no right node, left node becomes the root after root is deleted.
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val  # value is being copied actually.

            root.right = self.deleteNode(root.right,
                                         root.val)  # leftmost node in the right child tree is being deleted.

        return root