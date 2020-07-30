# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        result = ListNode(None)
        resultCurr = result

        while curr1 and curr2:
            if curr1.val < curr2.val:
                resultCurr.next = curr1
                curr1 = curr1.next
            else:
                resultCurr.next = curr2
                curr2 = curr2.next
            resultCurr = resultCurr.next

        if curr1:
            resultCurr.next = curr1

        if curr2:
            resultCurr.next = curr2

        return result.next
