# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # if the head element has to be removed, we can just go to the next element.If the below case for head if not
        # handled, we could try do prev.next = curr.next as well but then head does not really chnage,
        # we are changing only curr.
        while head and head.val == val:
            head = head.next

        curr = head
        prev = ListNode(None)
        prev.next = curr

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return head

