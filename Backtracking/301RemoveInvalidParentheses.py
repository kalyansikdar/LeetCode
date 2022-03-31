class Solution:
    def __init__(self):
        self.result = set()

    def removeInvalidParentheses(self, s):
        """
        This solution is TLE for Python in leetcode. But same java code works.
        """
        # gets the number of parentheses to be removed
        minimalRemovalNeeded = self.getMinimalRemoval(s)

        self._helper(s, minimalRemovalNeeded)

        return self.result

    def _helper(self, s, minRemovalNeededNow):
        # ignore duplicate element result, though set already ensures it
        if s in self.result:
            return
        # when no parenthesis is to be removed anymore
        if minRemovalNeededNow == 0:
            # if the s is still valid, add to the result
            if self.getMinimalRemoval(s) == 0:
                self.result.add((s))
                return

        for i in range(len(s)):
            left = s[0:i]
            right = s[i + 1:]
            # decrease minRemovalNeededNow as 1 parentheses is already taken care
            # left+right is the s without the current parentheses
            self._helper(left + right, minRemovalNeededNow - 1)

    def getMinimalRemoval(self, s):
        stack = []

        for ch in s:
            # push if it's a opening parenthesis
            if ch == '(':
                stack.append(ch)
            # if it's a closing parenthesis, if the stack is empty, add to stack and top is ')'
            # if the top is opening parenthesis, pop
            elif ch == ')':
                if len(stack) == 0:
                    stack.append(ch)
                elif stack[-1] == ')':
                    stack.append(ch)
                elif stack[-1] == '(':
                    stack.pop()

        # at the end extra parenthesis will be left in the stack
        return len(stack)


solution = Solution()
s = "()())()"
print(solution.removeInvalidParentheses(s))
assert solution.removeInvalidParentheses(s) == {"(())()","()()()"}
s = "(a)())()"
print(solution.removeInvalidParentheses(s))
assert solution.removeInvalidParentheses(s) == {"(a())()","(a)()()"}