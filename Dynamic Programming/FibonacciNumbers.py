class Solution:
    def fib(self, N: int) -> int:
        dp = [0] * (N + 1)
        # dp = [0 for i in range(N+1)]
        dp[0] = 0
        if N > 0:
            dp[1] = 1

        self.helper(N, dp)
        return dp[N]

    def helper(self, n, dp):
        if n <= 1:
            return n
        if dp[n] != 0:
            return dp[n]
        else:
            dp[n] = self.helper(n - 1, dp) + self.helper(n - 2, dp)
            return dp[n]


solution = Solution()
result = solution.fib(7)
print(result)

# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.