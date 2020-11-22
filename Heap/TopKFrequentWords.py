import heapq
import collections
from typing import List


class Element:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        """
        Compare two objects and find which one if greater (sorts by alphabetical order)
        :param other:
        :return:
        """
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.word == other.word and self.count == other.count

    def __repr__(self):
        return self.word + "-" + str(self.count)


class Solution:
    def topKFrequent(self, words, k: int):
        counts = collections.Counter(words)
        print(counts)
        heap = []
        heapq.heapify(heap)     # converts into a min heap

        for word, count in counts.items():
            heapq.heappush(heap, (Element(word, count), word))      # pushes each (word, count) combination into the
            # heap and sort by count and alphabetical order

            if len(heap) > k:
                heapq.heappop(heap)

        print('heap', heap)
        result = []
        while len(heap) > 0:
            x = heapq.heappop(heap)[1]
            print(x, heap)
            result.append(x)

        return result[::-1]     # as it's a mean heap word with lowest count will be on top, hence, reverse

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Slightly improved, Not storing the word in heap along with Element
        """
        freq = collections.Counter(words)

        heap = []
        heapq.heapify(heap)

        for word, count in freq.items():
            heapq.heappush(heap, Element(word, count))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while len(heap) > 0:
            result.append(heapq.heappop(heap).word)

        return result[::-1]


solution = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
# words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"] # k = 4
k = 2   # 3
print (solution.topKFrequent(words, k))