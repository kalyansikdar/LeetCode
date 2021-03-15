class Solution:
    def findMin(self, nums) -> int:
        if not nums:
            return None
        else:
            return self.binarySearch(nums, 0, len(nums) - 1)

    def binarySearch(self, nums, start, end):
        mid = start + (end - start) // 2

        while start < end:
            print(start, end, mid)
            if nums[mid] < nums[end]:
                return self.binarySearch(nums, start, mid)
            elif nums[mid] > nums[end]:
                return self.binarySearch(nums, mid + 1, end)
            else:  # if nums[mid] == nums[start] == nums[end] it becomes a linear search, decrease end by 1
                return self.binarySearch(nums, start, end - 1)

        return nums[start]


solution = Solution()
nums = [2, 2, 2, 0, 1]
nums = [1, 1]
print("Result: ", solution.findMin(nums))
