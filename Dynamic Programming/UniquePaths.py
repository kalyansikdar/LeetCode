class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result_matrix = [[0] * m for i in range(n)]
        # fill the first row with 1 as there is only one way to go to these boxes as you can come to there only from
        # left
        for i in range(m):
            result_matrix[0][i] = 1
        # there is only one way to go to these boxes as you can come to there only from up
        for i in range(n):
            result_matrix[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                result_matrix[i][j] = result_matrix[i - 1][j] + result_matrix[i][j - 1]

        return result_matrix[n - 1][m - 1]

    # This solution is better than the previous one
    def uniquePaths_Better(self, m: int, n: int) -> int:
        result_matrix = [[1] * m for i in range(n)]
        #  all boxes in first row and column should have 1  as there is 1 way to go into those, from TOP and from LEFT
        # rest of the boxes will be updated by the code below
        for i in range(1, n):
            for j in range(1, m):
                result_matrix[i][j] = result_matrix[i - 1][j] + result_matrix[i][j - 1]

        return result_matrix[n - 1][m - 1]

    # This solution is with Memoization
    def uniquePaths_Memoization(self, m: int, n: int) -> int:
        result_matrix = [[1] * m for i in range(n)]

        self.helper(n - 1, m - 1, result_matrix)
        return result_matrix[n - 1][m - 1]

    def helper(self, i, j, dp):
        if i == 0 or j == 0:
            return 1
        if dp[i][j] > 1:
            return dp[i][j]
        else:
            dp[i][j] = self.helper(i - 1, j, dp) + self.helper(i, j - 1, dp)
            return dp[i][j]


solution = Solution()
m, n = 7, 3
result_dp = solution.uniquePathsBetter(m, n)
print(result_dp)
result_memoization = solution.uniquePaths_Memoization(m, n)
print(result_memoization)
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right