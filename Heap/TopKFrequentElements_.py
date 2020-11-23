import collections
import heapq
from typing import List


class Element:
    def __init__(self, num, count):
        self.num = num
        self.count = count

    def __lt__(self, other):
        return self.count < other.count

    def __repr__(self):
        return str(self.num) + "-" + str(self.count)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []
        heapq.heapify(heap)

        for num, count in freq.items():
            heapq.heappush(heap, Element(num, count))

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        result = []
        while len(heap) > 0:
            result.append(heapq.heappop(heap).num)

        return result[::-1]


solution = Solution()
nums = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
nums1 = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums1, k))