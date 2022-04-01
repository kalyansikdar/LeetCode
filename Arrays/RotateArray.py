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

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse the array [7,6,5,4,3,2,1]
        # reverse the first k elements (index: k-1), reverse the rest k to n elements (index: (n-k) -> n)
        # base case
        if len(nums) == 1:
            return nums

        n = len(nums)
        # if k is larger than the length of array. Ex, k = 10, len = 7. Then the array has to be rotated actually 3
        # times, which is equivalent to rotating 3 times: 10 % 7 = 3
        k = k % n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(solution.rotate_bruteForce(nums, k))
