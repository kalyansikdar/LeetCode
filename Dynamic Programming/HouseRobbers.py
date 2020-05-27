class Solution:
    def rob(self, nums) -> int:
        dp = [0 for i in range(len(nums) + 1)]
        dp[1] = nums[0]
        # at every house we are calculating the max amount for the next house, hence the dp array has one more element
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[len(nums)]


solution= Solution()
nums = [7,3,2,5,9,1,1,12]
result = solution.rob(nums)
print (result)