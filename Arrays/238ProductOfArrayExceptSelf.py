class Solution:
    def productExceptSelf(self, nums):
        """
        Time Complexity: O(3N) ~ O(N) for 3 loops
        Space Complexity: O(2N) as output array is not considered
        ~ O(N)
        """
        # create two lists for storing cumuliative products from start and end
        startProduct, endProduct = [0] * len(nums), [0] * len(nums)

        initialProduct = 1

        for i in range(len(nums)):
            initialProduct *= nums[i]
            startProduct[i] = initialProduct

        initialProduct = 1

        for i in range(len(nums) - 1, -1, -1):
            initialProduct *= nums[i]
            endProduct[i] = initialProduct

        result = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = endProduct[i + 1]
            elif i == len(nums) - 1:
                result[i] = startProduct[i - 1]
            else:
                result[i] = startProduct[i - 1] * endProduct[i + 1]

        return result

    def productExceptSelf_better(self, nums):
        """
        Two iteration logic without extra space. First output array is filled with cumulative product till the
        second last element. For input = [1, 2, 3, 4]. Output after first iteration: [1, 1, 2, 6]. In the second
        iteration, iterate from end and multiple the output elements with i.
        """
        product = 1
        output = []

        for i in nums:
            output.append(product)
            product *= i

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output


solution = Solution()
nums = [2, 3, 5, 4]
assert solution.productExceptSelf(nums) == [60, 40, 24, 30]
nums = [1, 2, 3, 4]
assert solution.productExceptSelf(nums) == [24, 12, 8, 6]