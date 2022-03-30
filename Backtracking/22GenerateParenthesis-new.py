class Solution:
    def __init__(self):
        self.result = []
        self.stack = []

    def generateParenthesis(self, n: int):
        self.backtrack(0, 0, n)
        return self.result

    def backtrack(self, open, close, n):
        # valid parenthesis formed if open = close = n
        if open == n and close == n:
            copyString = "".join(self.stack)
            self.result.append(copyString)

        if open < n:
            self.stack.append("(");
            self.backtrack(open + 1, close, n)
            # backtracking
            self.stack.pop()

        # close > open is invalid - ignore
        # close = open -> ignore as adding ")" makes it invalid
        if close < open:
            self.stack.append(")")
            self.backtrack(open, close + 1, n)
            # backtracking
            self.stack.pop()


solution = Solution()
N = 3
expectedResult = ["((()))","(()())","(())()","()(())","()()()"]
assert solution.generateParenthesis(N) == expectedResult