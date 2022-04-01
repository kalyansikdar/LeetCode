class Solution(object):
    def _helper(self, n, s, open, close, result):
        close = len(s) - open

        if open == n and close == n:
            result.append(s)
        if open < n:
            self._helper(n, s + "(", open + 1, close, result)
        if close < open:
            self._helper(n, s + ")", open, close + 1, result)

    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open, close = 0, 0
        result = []
        s = ""
        if n < 1:
            return []
        else:
            self._helper(n, s, open, close, result)
            return result

    def generateParenthesis2(self, n: int):
        result = []
        self.backtrack(
            n, "", 0, 0, result
        )  # open, close both 0 as it at first n bracket is opened
        return result

    def backtrack(self, n, path, open, close, result):
        if len(path) == 2 * n:  # When the size of the string is 2n, it's valid parenthesis formation, add to result
            result.append(path)

        if open < n:
            self.backtrack(n, path + "(", open + 1, close, result)
        if close < open:  # bracket cannot be closed before it's opened, hence, close will always be smaller
            self.backtrack(n, path + ")", open, close + 1, result)


solution = Solution()
n = 3
print("Result 1: ", solution.generateParenthesis1(n))
print("Result 2: ", solution.generateParenthesis2(n))
