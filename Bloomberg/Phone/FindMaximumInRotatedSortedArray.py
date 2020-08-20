import sys
class Solution:
    def findMax(self, arr):
        """
        This is O(n) solution
        """
        maxVal = -sys.maxsize
        for num in arr:
            maxVal = max((maxVal, num))

        return maxVal

    def findMax_BinarySearch(self, arr):
        if not arr:
            return None
        else:
            return self.binarySearch(arr, 0, len(arr)-1)

    def binarySearch(self, nums, start, end):
        mid = start + (end - start)//2

        while start < end:
            if nums[mid] < nums[end]:
                return self.binarySearch(nums, start, mid)
            else:
                return self.binarySearch(nums, mid+1, end)

        return nums[end]


solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
nums = [6, 7, 0, 1, 2, 4, 5]
print(solution.findMax(nums))
assert solution.findMax([4, 5, 6, 7, 0, 1, 2]) == 7
assert solution.findMax([6, 7, 0, 1, 2, 4, 5]) == 7