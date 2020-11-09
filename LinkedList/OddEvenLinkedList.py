# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        curr = head
        even = ListNode(None)
        odd = ListNode(None)
        even_curr = even
        odd_curr = odd
        count = 0

        while curr:
            new_node = ListNode(curr.val)

            if count % 2:  # odd-even decision is based on the node number, not node value
                even_curr.next = new_node
                even_curr = even_curr.next
            else:
                odd_curr.next = new_node
                odd_curr = odd_curr.next
            curr = curr.next
            count += 1

        odd_curr.next = even.next  # Need to append the head of the even list
        return odd.next

    def oddEvenList_better(self, head: ListNode) -> ListNode:
        """
        Time complexity : O(n). There are total nn nodes and we visit each node once.
        Space complexity : O(1). All we need is the four pointers.
        :param head:
        :return:
        """
        if not head:
            return None

        odd = head
        evenHead = head.next  # even points to the second node
        even = evenHead  # pointer for even list

        # dry-run to understand
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head
