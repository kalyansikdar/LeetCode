# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # take two pointers, move one till n. If it reached end then this case: [1,2,3], n = 3
        # Once one pointer is moved n times, move both together till
        if not head:
            return None

        currA, currB = head, head
        # Take one pointer n nodes ahead
        while n and currB:
            currB = currB.next
            n -= 1
        # After going N nodes ahead, if currB is None, it means N nodes from last would be first node itself
        if not currB:
            return head.next
        # Move both till end, wherever currA stops, we have to delete the next node
        while currB.next:
            currB = currB.next
            currA = currA.next

        currA.next = currA.next.next

        return head