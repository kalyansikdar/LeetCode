class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for bracket in s:
            if bracket not in mappings:
                stack.append(bracket)
            else:
                if stack and mappings[bracket] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(bracket)

        return len(stack) == 0


solution = Solution()
s = "()[]{}"
assert solution.isValid(s) == True
s = ")(){}"
assert solution.isValid(s) == False
