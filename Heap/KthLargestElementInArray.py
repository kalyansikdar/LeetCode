import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

        heapq._heapify_max(heap)

        while k - 1:
            heapq.heappop(heap)
            heapq._heapify_max(heap)
            k -= 1

        return heap[0]

    def findKthLargest_Ologn(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)     # time complexity O(nlogn) as all n elements of nums are being heapified

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]

    def findKthLargest_Ologk(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)     # time complexity O(nlogk) as all k elements of nums are being heapified

        for i in nums[k:]:  # O(k)
            heapq.heappush(heap, i)
            heapq.heappop(heap)

        return heap[0]

    def findKthLargest_quickSelect(self, nums: List[int], k: int) -> int:
        """
        Time complexity: Quick Select
        Last element or random element is taken as Pivot. For each Pivot element, it's right sorted index is selected
        i.e. in O(N) iteration. Then one half is selected -> left or right.
        On average case, at every iteration search space is being halfed.
        n + n/2 + n/4..... + 1 = 2N
        But in the worst case, if the array is sorted in a decreasing manner, it will be n^2
        """
        # adjust k to calculate from end (?)
        k = len(nums) - k
        return self.quickSelect(0, len(nums) - 1, nums, k)

    def quickSelect(self, start, end, nums, k):
        # take last element as pivot
        pivot = nums[end]
        # pivot index -> 0 or the start index
        p = start

        for i in range(start, end):
            if nums[i] <= pivot:
                # swap elements at (i, p)
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        # end of the loop, p index will denote to the right position of the pivot element
        nums[p], nums[end] = nums[end], nums[p]

        # If pivot index is greater than k, means kth largest element is on the left side of p
        if p > k:
            return self.quickSelect(start, p - 1, nums, k)
        elif p < k:
            return self.quickSelect(p + 1, end, nums, k)
        else:
            # if pivot index is equal to k, return the pivot element
            return nums[p]


solution = Solution()
nums, k = [3,2,1,5,6,4], 2
assert solution.findKthLargest_Ologk(nums, k) == 5
nums, k = [3,2,3,1,2,4,5,5,6], 4
assert solution.findKthLargest_Ologk(nums, k) == 4
nums, k = [3,2,1,5,6,4], 2
assert solution.findKthLargest_quickSelect(nums, k) == 5
nums, k = [3,2,3,1,2,4,5,5,6], 4
assert solution.findKthLargest_quickSelect(nums, k) == 4