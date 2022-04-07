# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        curr = head
        nodeCount = 0

        while curr:
            curr = curr.next
            nodeCount += 1

        if nodeCount == 1:
            return head

        # update the nodeCount to half, for even, point to second node
        if nodeCount % 2 == 0:
            nodeCount = (nodeCount / 2) + 1
        else:
            nodeCount = (nodeCount + 1) // 2

        # reset the curr to head
        curr = head
        while nodeCount - 1:
            curr = curr.next
            nodeCount -= 1

        return curr

    def middleNode_better(self, head):
        """
        Better approach with slow and fast runner
        """
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            slow = slow.next

        return slow