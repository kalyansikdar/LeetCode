# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n) - as stack used holds number of elements
    Algo:
    1. while root is not null, go left till root is not null. while going left, keep adding the node to the stack
    2. Once you can't go to left anymore, pop one node from stack and go right, then repeat step 1
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        curr = root

        while curr or stack:
            while curr:
                # go left till root is not none
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)

            curr = curr.right

        return result