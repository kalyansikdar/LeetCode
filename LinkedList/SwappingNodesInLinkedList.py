# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # using 2 pointers find kth node from last
        curr = head

        while k - 1:
            curr = curr.next
            k -= 1

        # place second pointer at head and move it along with kCurr till last
        # then second pointed with be at k from last index
        kCurr = curr
        second = head

        while kCurr.next:
            kCurr = kCurr.next
            second = second.next

        # Swap the nodes
        curr.val, second.val = second.val, curr.val

        return head

