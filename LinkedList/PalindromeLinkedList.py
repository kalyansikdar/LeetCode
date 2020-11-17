# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, value):
        self.head = value

    def addAtEnd(self, node):
        curr = self.head
        new_node = ListNode(node)
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def __repr__(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


class Solution:
    def isPalindrome(self, head) -> bool:
        curr = head
        stack = []

        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head

        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next

        return True

    def print(self, head):
        curr = head

        while curr:
            print(curr.val)
            curr = curr.next

    def isPalindrome_better(self, head: ListNode) -> bool:
        """
        Algorithm:
        1. Apply fast and slow runner to find the middle of the list. When fast runner reaches last node,
        slow will be on the middle node or middle-before node.
        2. If fast, means length of list is odd, hence, move slow another node
        3. Reverse list from slow pointer and assign to slow, so it will point to the reversed list
        4. Assign head to fast (re-initializing)
        5. Check if each node's value is same

        Time complexity: O(N)
        Space complexity: O(1)
        :param head:
        :return:
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:    # if length of list is odd, then fast will be on the last node, so, slow will be just one node
            # before middle node. Else fast will be NULL.
            slow = slow.next

        slow = self.reverse(slow)   # reverse the list from middle and assign it to slow
        fast = head     # re-initialize head to fast

        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True

    def reverse(self, head):
        curr = head
        prev = next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


linkedList = LinkedList(None)
linkedList.addAtEnd(3)
linkedList.addAtEnd(6)
linkedList.addAtEnd(9)
print(linkedList)

# assert solution.findMax([4, 5, 6, 7, 0, 1, 2]) == 7
# assert solution.findMax([6, 7, 0, 1, 2, 4, 5]) == 7