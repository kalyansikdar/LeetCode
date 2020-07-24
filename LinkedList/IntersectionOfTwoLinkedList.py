# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB = headB
        lenA, lenB = 0, 0

        while currA:
            currA = currA.next
            lenA += 1

        while currB:
            currB = currB.next
            lenB += 1

        currA, currB = headA, headB

        if lenB > lenA:
            currA, currB = currB, currA

        diff = abs(lenB - lenA)

        while diff:
            currA = currA.next
            diff -= 1

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA

    def getIntersectionNode_twoPointers(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Check the comment which explains the solution visially -
        https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
        """
        currA = headA
        currB = headB

        while currA != currB:
            if not currA:
                currA = headB       # When currA reaches the end of the list, then redirect it to the head of B
            else:
                currA = currA.next

            if not currB:
                currB = headA       # similarly when currB reaches the end of a list, redirect it the head of A.
            else:
                currB = currB.next

        return currA