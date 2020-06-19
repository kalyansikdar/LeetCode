class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


solution = Solution()
nums = [2, 0, 1, 2, 0, 1]
solution.sortColors(nums)
print(nums)