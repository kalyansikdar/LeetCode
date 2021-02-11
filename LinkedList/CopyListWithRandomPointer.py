# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr = head.next
        newHead = Node(head.val)
        prev = newHead  # curr is the second node(head.next)

        mappings = {head: newHead}

        while curr:
            newNode = Node(curr.val)
            prev.next = newNode  # assigning the next pointer

            mappings[curr] = newNode  # add current node and it's sibling node(with next and random as null)

            curr = curr.next
            prev = prev.next

        oldCurr = head
        newCurr = newHead

        while oldCurr:
            # for node 7, random is null, hence, this condition is needed
            newCurr.random = mappings[oldCurr.random] if oldCurr.random else None
            oldCurr = oldCurr.next
            newCurr = newCurr.next

        return newHead
