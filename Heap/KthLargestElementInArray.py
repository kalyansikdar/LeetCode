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


solution = Solution()
nums, k = [3,2,1,5,6,4], 2
assert solution.findKthLargest_Ologk(nums, k) == 5
nums, k = [3,2,3,1,2,4,5,5,6], 4
assert solution.findKthLargest_Ologk(nums, k) == 4