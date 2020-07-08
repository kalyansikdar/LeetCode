class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()      # needs to be sorted as it's an ordered integer list

    def findMedian(self) -> float:
        mid = (0 + len(self.stream)) // 2
        if len(self.stream) % 2 == 0:
            return (self.stream[mid - 1] + self.stream[mid]) / 2
        else:
            return self.stream[mid]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()