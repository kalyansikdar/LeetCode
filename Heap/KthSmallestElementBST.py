import heapq
from _heapq import heappop
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k) -> int:
        heap = []
        self.inorder_traversal(root, heap)      # get the elements in a list so that heap properties can be applied
        heapq.heapify(heap)     # heapify to form a min heap (default)

        while k - 1:        # pop k-1 elements so that the top element is the kth smallest one
            heappop(heap)
            k -= 1

        return heap[0]

    def inorder_traversal(self, root, result):
        if root:
            result.append(root.val)
            self.inorder_traversal(root.left, result)
            self.inorder_traversal(root.right, result)
