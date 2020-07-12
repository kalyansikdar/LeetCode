import heapq
import collections


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
            result.append(heapq.heappop(heap)[1])

        return result[::-1]     # as it's a mean heap word with lowest count will be on top, hence, reverse


solution = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
print (solution.topKFrequent(words, k))