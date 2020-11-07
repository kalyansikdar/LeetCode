# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr = head
        slow, fast = curr, curr
        flag = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = 1
                break

        # if there is not cycle, we have to return null
        if not flag:
            return None

        # if there is a cycle we are using 2 pointers, once from start, another from where slow and fast met. The
        # start of the loop will be at equal distance from the points.
        p1 = curr
        p2 = slow

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1
