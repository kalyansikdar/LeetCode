import heapq
from _heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, num)
        heapq._heapify_max(self.maxHeap)
        topOfMax = heappop(self.maxHeap)
        heappush(self.minHeap, topOfMax)
        heapq.heapify(self.minHeap)

        if len(self.maxHeap) < len(self.minHeap):
            topOfMin = heappop(self.minHeap)
            heappush(self.maxHeap, topOfMin)
            # heapq._heapify_max(self.maxHeap)

    def findMedian(self) -> float:
        print(self.maxHeap, self.minHeap)
        heapq._heapify_max(self.maxHeap)
        heapq.heapify(self.minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[-1]
        else:
            return (self.maxHeap[-1] + self.minHeap[0]) / 2


solution = MedianFinder()
solution.addNum(1)
print (solution.findMedian())
solution.addNum(2)
print(solution.findMedian())
solution.addNum(3)
print(solution.findMedian())
solution.addNum(4)
print (solution.findMedian())
solution.addNum(5)
print(solution.findMedian())
solution.addNum(6)
print(solution.findMedian())
solution.addNum(7)
print (solution.findMedian())
solution.addNum(8)
print(solution.findMedian())
solution.addNum(9)
print(solution.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()