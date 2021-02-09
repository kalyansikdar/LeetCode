# Definition for a binary tree node.
from binarytree import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionII:
    def __init__(self):
        self.totalCount = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)

            self.totalCount += root.val
            root.val = self.totalCount

            self.convertBST(root.left)

        return root


class Solution:
    def __init__(self):
        self.index = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        allNodeIndex = {}
        if not root:
            return None
        else:
            self.assignIndex(root, allNodeIndex)
            self._convertBST(root, allNodeIndex)
        return root

    def _convertBST(self, root, allNodeIndex):
        if root:
            newVal = 0

            for k in allNodeIndex:
                if k > root.val:
                    newVal += k

            root.val += newVal # key to be converted - original key plus sum of all keys greater than the original key in BST.

            self._convertBST(root.left, allNodeIndex)
            self._convertBST(root.right, allNodeIndex)

    def assignIndex(self, root, allNodeIndex):
        """
        Assigns index to all node and create a dict where {node.val: counter}
        """
        if root:
            self.assignIndex(root.left, allNodeIndex)
            allNodeIndex[root.val] = self.index
            self.index += 1
            self.assignIndex(root.right, allNodeIndex)


t1 = build([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
print(t1)
solution = Solution()
result = solution.convertBST(t1)
print (result)
# result [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
# t1 = build([0,None,1])
# result: [1,null,1]
# t1 = [3,2,4,1]
# result: [7,9,4,10]