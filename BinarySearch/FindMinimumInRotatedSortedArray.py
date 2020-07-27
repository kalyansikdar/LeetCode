class Solution:
    def findMin(self, nums) -> int:
        if not nums:
            return None
        else:
            return self.binarySearch(nums, 0, len(nums) - 1)

    def binarySearch(self, nums, start, end):
        mid = (start + end) // 2

        while start < end:
            if nums[mid] < nums[end]:
                return self.binarySearch(nums, start, mid)
            else:
                return self.binarySearch(nums, mid + 1, end)

        return nums[start]


solution = Solution()
nums = [4,5,6,7,0,1,2]
nums = [6,7,0,1,2,4,5]
print (solution.findMin(nums))