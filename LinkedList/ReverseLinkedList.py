# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __int__(self):
        self.head = ListNode(None)

    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        next = None
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
