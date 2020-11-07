# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr = head
        slow = curr
        fast = curr

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def __repr__(self):
        curr = self.head
        result = ""
        while curr:
            result += str(curr.val) + " "
            curr = curr.next

        return result


ll = Solution()
# Test Case # 1
# ll.addAtHead(1)
# print(ll)
# ll.addAtTail(3)
# print(ll)
# ll.addAtIndex(1,2)
# print(ll)
# print(ll.get(1))
# ll.deleteAtIndex(1)
# print(ll)
# print(ll.get(1))