import heapq


class MedianFinder:

    def __init__(self):
        # take two heaps, one max heap holds smaller half of numbers
        # another min heap, holds larger half of the numbers
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        # always push the number into the first heap
        # multiply by two as Python's default heap implementation is a min heap
        heapq.heappush(self.smaller, -1 * num)

        # if top element in maxHeap/smaller is greater than top element in minHeap/larger heap
        # it's against our assumption that every number in larger will be greater than the smaller
        if self.smaller and self.larger and (-1 * self.smaller[0]) > self.larger[0]:
            popped = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, popped)

        # size difference between the two heaps can be maximum 1
        # if the difference is bigger than 1, pop from the longer one and push into other one
        if len(self.smaller) - len(self.larger) >= 2:
            popped = -1 * heapq.heappop(self.smaller)
            heapq.heappush(self.larger, popped)

        if len(self.larger) - len(self.smaller) >= 2:
            popped = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -1 * popped)

    def findMedian(self) -> float:
        # if both heaps are not equal, median is the top element in the longer one
        if len(self.smaller) - len(self.larger) == 1:
            return -1 * self.smaller[0]

        if len(self.larger) - len(self.smaller) == 1:
            return self.larger[0]

        # if heap size are equal, return the avg of the top elements
        return (-1 * self.smaller[0] + self.larger[0]) / 2


solution = MedianFinder()
solution.addNum(1)
solution.addNum(2)
assert solution.findMedian() == 1.5
solution.addNum(3)
assert solution.findMedian() == 2
solution.addNum(4)
assert solution.findMedian() == 2.5
solution.addNum(5)
assert solution.findMedian() == 3
solution.addNum(6)
assert solution.findMedian() == 3.5
solution.addNum(7)
assert solution.findMedian() == 4