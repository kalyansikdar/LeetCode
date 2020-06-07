import heapq
from _heapq import heappush, heappop


class KthLargest:
    def __init__(self, k: int, nums):
        self.stream = nums
        self.k = k

        heapq.heapify(self.stream)
        # as we need to find k'th largest element, we would only keep elements greater than or equal to k using a min
        # heap, so the top element will be kth largest
        while len(self.stream) > k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heappush(self.stream, val)
        elif val > self.stream[0]:      # if the new value is greater than the smallest element in the min heap,
            # then it's one of the largest elements greater than kth. else it's even smaller, ignore it
            heappop(self.stream)
            heappush(self.stream, val)

        return self.stream[0]


kthLargest = KthLargest(3,[4,5,8,2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))

# Expected answer [4,5,5,8,8]