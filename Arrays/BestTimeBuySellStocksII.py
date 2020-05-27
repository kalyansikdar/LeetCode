class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        if not prices:
            return prices

        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit


solution = Solution()
prices = [7,1,5,3,6,4]
result = solution.maxProfit(prices)
print (result)