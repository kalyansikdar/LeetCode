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


linkedList = LinkedList(None)
linkedList.addAtEnd(3)
linkedList.addAtEnd(6)
linkedList.addAtEnd(9)
print(linkedList)

# assert solution.findMax([4, 5, 6, 7, 0, 1, 2]) == 7
# assert solution.findMax([6, 7, 0, 1, 2, 4, 5]) == 7