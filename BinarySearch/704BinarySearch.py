class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            return self.binary_search_iterative(0, len(nums) - 1, nums, target)

    def binary_search_iterative(self, start, end, nums, target):
        index = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                index = mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return index

    def binary_search(self, start, end, nums, target):
        mid = (start + end) // 2

        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary_search(mid + 1, end, nums, target)
            else:
                return self.binary_search(start, mid - 1, nums, target)

        return -1


solution = Solution()
arr = [-1,0,3,5,9,12]
target = 2
solution.search(arr, target) == -1
target = 9
solution.search(arr, target) == 4