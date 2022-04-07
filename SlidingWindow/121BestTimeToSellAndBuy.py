class Solution:
    def maxProfit(self, prices) -> int:
        # sliding window problem
        # Two pointer approach
        # left points to the min price
        # TC: O(n), SC: O(1)
        minPrice, pointer = 0, 1
        maxProfit = 0

        while pointer < len(prices):
            # check if profitable
            if prices[pointer] > prices[minPrice]:
                maxProfit = max(maxProfit, prices[pointer] - prices[minPrice])
            else:
                # update the min price pointer as we found a lesser price
                minPrice = pointer

            pointer += 1

        return maxProfit


solution = Solution()
prices = [7,1,5,3,6,4]
assert solution.maxProfit(prices) == 5