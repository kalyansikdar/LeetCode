class Solution:
    def maxSubArray(self, nums) -> int:
        maxVal_tillNow = nums[0]
        max_val = nums[0]

        for i in range(1, len(nums)):
            if maxVal_tillNow > max_val:
                max_val = maxVal_tillNow
            maxVal_tillNow = max(maxVal_tillNow + nums[i], nums[i])

        # This is needed for test case [-1, 5]
        if maxVal_tillNow > max_val:
            max_val = maxVal_tillNow
        return max_val

    def maxSubArray_better(self, nums) -> int:
        # Superb solution: Did it myself.
        # TC: O(N)
        maxTillEnd = nums[0]
        maxTillHere = nums[0]

        for i in range(1, len(nums)):
            maxTillHere = max(nums[i], maxTillHere + nums[i])
            maxTillEnd = max(maxTillHere, maxTillEnd)

        return maxTillEnd


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = solution.maxSubArray(nums)
print(result)