class Solution:
    def sortedSquares(self, nums):
        # Use two pointers
        # Square both elements, store the bigger one at the end index
        # initialize the result array with 0
        result = [0] * len(nums)
        start, end = 0, len(nums) - 1
        resultEnd = len(nums) - 1

        while start <= end:
            if nums[start] * nums[start] > nums[end] * nums[end]:
                result[resultEnd] = nums[start] * nums[start]
                start += 1

            else:
                result[resultEnd] = nums[end] * nums[end]
                end -= 1

            resultEnd -= 1

        return result


solution = Solution()
nums = [-4,-1,0,3,10]
assert solution.sortedSquares(nums) == [0,1,9,16,100]
nums = [-5,-3,-2,-1]
assert solution.sortedSquares(nums) == [1, 4, 9, 25]