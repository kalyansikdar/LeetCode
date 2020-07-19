# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        """
        Time complexity O(n) to create the BST for inorder traversal
        :param root:
        """
        self.sortedNodes = []       # elements will be sorted in this list as its added using inorder traversal
        self.index = 0
        self.inorder(root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.sortedNodes.append(root.val)
            self.inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.sortedNodes[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 <= len(self.sortedNodes)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()