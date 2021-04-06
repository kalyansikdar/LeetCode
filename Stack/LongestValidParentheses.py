class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0

        for i in range(len(s)):
            ch = s[i]

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    longest = max(longest, length)

        return longest


solution = Solution()
s = ")()())"
assert solution.longestValidParentheses(s) == 4
s = "(()()((())))"
assert solution.longestValidParentheses(s) == 12