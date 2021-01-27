# Definition for singly-linked list.
import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        dummy = head = ListNode(None)
        for curr in lists:
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        while len(heap) > 0:
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next

        return head.next

    def mergeKLists_Not_better_TC(self, lists: List[ListNode]) -> ListNode:
        """
        Time complexity for heap push is O(logn).
        Hence overall, for inserting into heap TC is O(n)*O(n)*O(logn) ~ O(n^2*logn)
        Then, popping from the heap O(logn)

        Overall O(n^2*logn)
        """
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]

        heap = []
        dummy = head = ListNode(None)
        entryCount = 0
        for curr in lists:
            while curr:
                entryCount += 1  # Tuple comparison breaks for (priority, task) pairs if the priorities are equal and
                # the tasks do not have a default comparison order. Solution is to store entries as 3-element list
                # including the priority, an entry count, and the task. The entry count serves as a tie-breaker so
                # that two tasks with the same priority are returned in the order they were added.
                heapq.heappush(heap, (curr.val, entryCount, curr))
                curr = curr.next

        while len(heap) > 0:
            dummy.next = heapq.heappop(heap)[2]
            dummy = dummy.next

        return head.next