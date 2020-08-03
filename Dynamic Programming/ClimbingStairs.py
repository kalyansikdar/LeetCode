class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This is the actual solution
        :param n:
        :return:
        """
        memo = [0] * (n + 1)

        if n <= 0:      # considering there is 1 way if n is 0 or -ve i.e. you can do nothing
            return 0
        if n <= 2:      # there is n ways to climb n stairs if n = 1 or 2
            return n
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return memo[n]

    def climbStairs_later(self, n: int) -> int:
        """
        This was done randomly some time using dp
        :param n:
        :return:
        """
        dp = [0] * (n + 1)
        self._climbStairs(n, dp)
        print(dp)
        return dp[n]

    def _climbStairs(self, n, dp):
        if dp[n] > 0:
            return dp[n]
        elif n <= 3:
            dp[n] = n
            return n
        else:
            res = self._climbStairs(n - 1, dp) + self._climbStairs(n - 2, dp)
            dp[n] = res
            return res


solution = Solution()
result = solution.climbStairs_later(7)
print(result)
# Question
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step