# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        if not root:
            return result
        else:
            self.getTree(root, result)

        serializedTree = " ".join(result)

        return serializedTree

    def getTree(self, root, result):
        if root:
            result.append(str(root.val))
            self.getTree(root.left, result)
            self.getTree(root.right, result)
        else:
            result.append('None')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []

        treeList = data.split(" ")

        return self._deserialize(treeList)

    def _deserialize(self, treeList):
        if treeList[0] == 'None':
            treeList.pop(0)
            return None

        root = TreeNode(treeList[0])
        treeList.pop(0)

        root.left = self._deserialize(treeList)
        root.right = self._deserialize(treeList)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))