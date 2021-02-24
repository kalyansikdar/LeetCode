import heapq
from typing import List


class HeapEntry:
    def __init__(self, length, word):
        self.length = length
        self.word = word

    def __lt__(self, other):
        if self.length == other.length:
            return self.word > other.word
        return self.length < other.length


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        """
        Time complexity: 
        """
        heap = []
        # for every word, check if it can be formed from the dict
        # if yes, add to a heap, heap will sort the items lexicographically
        for word in d:
            if self.canFormFromDict(s, word):
                # print (word)
                heapq.heappush(heap, HeapEntry(len(word), word))

        # if there is no word that can be formed, return ""
        if not heap:
            return ""
        # max heapify as default is mean heap
        heapq._heapify_max(heap)
        # pop the top element
        return heapq.heappop(heap).word

    def canFormFromDict(self, s, word):
        i, j = 0, 0

        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1

        if j == len(word):
            return True
        else:
            return False


solution = Solution()
s = "abpcplea"
d = ["ale","apple","monkey","plea"]
assert solution.findLongestWord(s, d) == "apple"
s = "abpcplea"
d= ["a","b","c"]
assert solution.findLongestWord(s, d) == "a"