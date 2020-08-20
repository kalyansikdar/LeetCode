class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """
        This solution is O(n) time complexity, O(n) space complexity
        :param S:
        :return:
        """
        minToAdd = 0
        stack = []
        mapping = {
            ')': '('
        }

        for ch in S:
            if ch == '(':
                stack.append(ch)
            elif ch == ')' and stack and stack[-1] == mapping[ch]:
                stack.pop()
            else:
                minToAdd += 1
        return minToAdd + len(stack)

    def minAddToMakeValid_Better(self, S: str) -> int:
        open = 0
        minToAdd = 0

        for ch in S:
            if ch == '(':
                open += 1
            elif ch == ')' and open > 0:
                open -= 1
            else:
                minToAdd += 1

        return minToAdd + open


solution = Solution()
S = "()))(("
print(solution.minAddToMakeValid_Better(S))

# Example 1:

# Input: "())"
# Output: 1
# Example 2:
#
# Input: "((("
# Output: 3
# Example 3:
#
# Input: "()"
# Output: 0
# Example 4:
#
# Input: "()))(("
# Output: 4