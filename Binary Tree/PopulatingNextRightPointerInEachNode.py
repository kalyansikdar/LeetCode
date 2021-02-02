# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Time complexity O(n) as it's going through each node
        """
        if not root:
            return None

        leftNode = root

        while leftNode.left:
            curr = leftNode

            while curr:
                curr.left.next = curr.right

                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next

            leftNode = leftNode.left

        return root
