# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head

        while curr:
            if not curr.child:
                curr = curr.next
                continue

            temp = curr.child

            while temp.next:
                temp = temp.next
            # This condition is required if curr is the last node in that level, so there is no curr.next
            if curr.next:
                curr.next.prev = temp

            temp.next = curr.next
            # The prev node of the child node would be the current node as the child is not child anymore
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

        return head
