import collections
import heapq
import string
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()  # Converts every string elements to lower case
        for ch in string.punctuation:
            paragraph = paragraph.replace(ch, ' ')  # Replaces all punctuations by ' '

        words = paragraph.split()
        freq = collections.Counter(words)  # creates a map with frequency of key's occurance
        heap = []
        heapq.heapify(heap)  # creates a min heap

        for item, count in freq.items():
            if item not in banned:
                heapq.heappush(heap, (-count, item))  # Elements within heap will be ordered automatically by the first
                # element. Count is considered negative as it's a min-heap

        return heapq.heappop(heap)[1]  # pops the top-most element and returns the 1st element of the object


solution = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
assert solution.mostCommonWord(paragraph, banned) == "ball"