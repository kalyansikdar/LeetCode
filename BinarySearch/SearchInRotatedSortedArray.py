class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        else:
            return self.binarySearch(nums, target, 0, len(nums) - 1)

    def binarySearch(self, nums, target, start, end):
        mid = start + (end - start) // 2

        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:  # left side is strictly increasing
                if (
                    target <= nums[mid] and target >= nums[start]
                ):  # if the target falls within start to end
                    return self.binarySearch(nums, target, start, mid - 1)
                else:
                    return self.binarySearch(nums, target, mid + 1, end)
            else:  # right side is strictly increasing
                if (
                    target >= nums[mid] and target <= nums[end]
                ):  # if target falls within mid to end
                    return self.binarySearch(nums, target, mid + 1, end)
                else:
                    return self.binarySearch(nums, target, start, mid - 1)

        return -1


solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(solution.search(nums, target))
