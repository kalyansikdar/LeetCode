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