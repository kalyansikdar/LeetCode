# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        resHead = ListNode(None)
        resCurr = resHead

        while curr1 and curr2:
            if curr1.val < curr2.val:
                resCurr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                resCurr.next = ListNode(curr2.val)
                curr2 = curr2.next

            resCurr = resCurr.next

        if curr1:
            resCurr.next = curr1
        if curr2:
            resCurr.next = curr2

        return resHead.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        resHead = ListNode(None)
        resCurr = resHead

        while curr1 and curr2:
            if curr1.val < curr2.val:
                resCurr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                resCurr.next = ListNode(curr2.val)
                curr2 = curr2.next

            resCurr = resCurr.next

        resCurr.next = curr1 or curr2

        return resHead.next

    def mergeTwoLists_better(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        This solution is in-place and NOT using extra variable
        :param l1:
        :param l2:
        :return:
        """
        curr1 = l1
        curr2 = l2
        resCurr = ListNode(None)
        resHead = resCurr

        while curr1 and curr2:
            if curr1.val < curr2.val:
                resCurr.next = curr1
                curr1 = curr1.next
            else:
                resCurr.next = curr2
                curr2 = curr2.next

            resCurr = resCurr.next

        resCurr.next = curr1 or curr2

        return resHead.next