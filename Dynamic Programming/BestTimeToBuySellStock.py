class Solution:
    '''
    This is O(N2) solution
    '''
    def maxProfit(self, prices) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit


solution = Solution()
nums = [7,1,5,3,6,4]
result = solution.maxProfit(nums)
print(result)


# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.