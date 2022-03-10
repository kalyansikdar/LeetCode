class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if not nums:
            return None
        else:
            return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearch(self, nums, target, start, end):
        mid = start + (end - start) // 2

        while (
            start <= end
        ):  # as we are using <= start position can actually be greater than end at the end of the
            # iteration
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return self.binarySearch(nums, target, start, mid - 1)
            else:
                return self.binarySearch(nums, target, mid + 1, end)

        return start
