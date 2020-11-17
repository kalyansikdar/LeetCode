# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        reminder = 0
        resHead = ListNode(None)
        resCurr = resHead

        while curr1 or curr2:
            temp = reminder
            if curr1:
                temp += curr1.val
                curr1 = curr1.next

            if curr2:
                temp += curr2.val
                curr2 = curr2.next

            if temp > 9:
                reminder = 1
            else:
                reminder = 0

            add_val = temp % 10
            resCurr.next = ListNode(add_val)
            resCurr = resCurr.next

        if reminder:
            resCurr.next = ListNode(reminder)

        return resHead.next