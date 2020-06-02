import sys
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True
        else:
            return self.checkValidity(root, -sys.maxsize + 1, sys.maxsize)

    def checkValidity(self, root, leftLimit, rightLimit):
        if root:
            left_val = root.left.val if root.left else leftLimit
            right_val = root.right.val if root.right else rightLimit
            print ('values:' , left_val, root.val, right_val)
            if left_val < root.val < right_val:
                return self.checkValidity(root.left, leftLimit, root.val) and self.checkValidity(root.right, root.val,
                                                                                                 rightLimit)
            else:
                return False
        else:
            return True

    def get_tree(self, arr):
        if len(arr) is None:
            return None

        if len(arr) == 1:
            return TreeNode(arr[0])

        mid = int(len(arr) / 2)

        root = TreeNode(arr[mid])
        root.left = self.get_tree(arr[:mid])
        print(arr[:mid], arr[mid], arr[mid + 1:])
        if len(arr) == 2:
            return root
        root.right = self.get_tree(arr[mid + 1:])

        return root


solution = Solution()
tree = solution.get_tree([10,5,15,None,None,6,20])
print ('tree:', tree)
result = solution.isValidBST(tree)
print (result)
