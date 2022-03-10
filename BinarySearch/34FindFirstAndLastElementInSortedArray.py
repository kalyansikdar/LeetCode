class Solution:
    def searchRange(self, nums, target: int):
        result = []
        result.append(self.searchFirstPosition(nums, target, 0, len(nums) - 1))
        result.append(self.searchLastPosition(nums, target, 0, len(nums) - 1))

        return result

    def searchFirstPosition(self, nums, target, start, end):
        index = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                index = mid

            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return index

    def searchLastPosition(self, nums, target, start, end):
        index = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                index = mid

            if target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return index


solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 7
solution.searchRange(nums, target)
