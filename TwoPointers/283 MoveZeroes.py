class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This algorithm is similar to quick select/quick sort
        # Time complexity: O(N)
        # In place solution
        left = 0
        right = 0

        while right < len(nums):

            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1