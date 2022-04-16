class NumArray:
    def __init__(self, nums):
        # array representing a segment tree.
        # (4n+1) is the maximum number of nodes in a perfect binary tree
        # Few spaces might be left empty if it's not a perfect BT
        self.segmentTree = [0] * (4 * len(nums) + 1)
        self.stIndex = 1
        self.start = 0
        self.end = len(nums) - 1

        self.buildST(self.stIndex, nums, self.start, self.end)
        # print(self.segmentTree)

    def buildST(self, stIndex, nums, start, end):
        # base case
        if start > end:
            return

            # leaf node
        if start == end:
            self.segmentTree[stIndex] = nums[start]  # or nums[end]
            return

        # internal node
        mid = start + (end - start) // 2
        # populate left and right trees
        # indices of child nodes will be at 2i and 2i+1 indices
        self.buildST(2 * stIndex, nums, start, mid)
        self.buildST(2 * stIndex + 1, nums, mid + 1, end)

        self.segmentTree[stIndex] = self.segmentTree[2 * stIndex] + self.segmentTree[2 * stIndex + 1]

    def update(self, index: int, val: int) -> None:
        self.updateNode(self.stIndex, self.start, self.end, index, val)

    def updateNode(self, stIndex, start, end, index, newVal):
        # no overlap
        if start > index or end < index:
            return

        # total overlap
        if start == end:
            self.segmentTree[stIndex] = newVal
            return

        # internal node.. partial overlap
        mid = start + (end - start) // 2

        self.updateNode(2 * stIndex, start, mid, index, newVal)
        self.updateNode(2 * stIndex + 1, mid + 1, end, index, newVal)

        self.segmentTree[stIndex] = self.segmentTree[2 * stIndex] + self.segmentTree[2 * stIndex + 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.getSumRange(left, right, self.stIndex, self.start, self.end)

    def getSumRange(self, rangeStart, rangeEnd, stIndex, start, end):
        # No overlap case
        if rangeStart > end or rangeEnd < start:
            return 0

        # total overlap. whole start to end array is required for the query range
        if start >= rangeStart and end <= rangeEnd:
            return self.segmentTree[stIndex]

        # partial overlap
        mid = start + (end - start) // 2
        leftSum = self.getSumRange(rangeStart, rangeEnd, 2 * stIndex, start, mid)
        rightSum = self.getSumRange(rangeStart, rangeEnd, 2 * stIndex + 1, mid + 1, end)

        return leftSum + rightSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


array = [1, 2, 3, 4, 5, 6]
solution = NumArray(array)
assert solution.segmentTree == [0, 21, 6, 15, 3, 3, 9, 6, 1, 2, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert solution.sumRange(3, 6) == 15
solution.update(2, 100)     # input array is now: [1, 2, 100, 4, 5, 6]
assert solution.segmentTree == [0, 118, 103, 15, 3, 100, 9, 6, 1, 2, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert solution.sumRange(2, 4) == 109
