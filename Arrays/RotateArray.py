class Solution:
    def rotate_bruteForce(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        for i in range(k):
            temp = nums[len(nums) - 1]
            for j in range(len(nums) - 1 - 1, -1, -1):
                nums[j + 1] = nums[j]
            nums[j] = temp

        return nums

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        # in case k is greater than len(nums) then we need to rotate only k%len(nums) time.. ex nums = [1,2], k = 3,
        # then need to rotate only 3%2 = 1 time
        k = k % len(nums)
        print(k)

        self.reverse(nums, 0, len(nums) - k - 1)
        print(nums)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        print(nums)
        self.reverse(nums, 0, len(nums) - 1)
        print(nums)

        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(solution.rotate_bruteForce(nums, k))
