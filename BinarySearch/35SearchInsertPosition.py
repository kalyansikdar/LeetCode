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

        def findInsertPosition(self, nums, start, end, target):
            # OWN method: Focus is to find the insert position. If mid-1 is less and mid+1 is larger, that's
            # the position but within that condition, should the insert position is before mid or after mid
            # like this ex: [1, 3, 5], target = 4. Here, (mid-1) < 4 < (mid+1). But it has to be placed after 3.
            # hence, the if condition within the if condition is needed.
            mid = start + (end - start) // 2

            while start <= end:
                if mid > 0 and mid < len(nums) - 1 and nums[mid - 1] < target and nums[mid + 1] > target:
                    if target > nums[mid]:
                        return mid + 1
                    else:
                        return mid
                else:
                    if target > nums[mid]:
                        return self.findInsertPosition(nums, mid + 1, end, target)
                    else:
                        return self.findInsertPosition(nums, start, mid - 1, target)

            return start

        return start
