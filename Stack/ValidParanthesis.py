class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for ch in s:
            if ch not in mappings:
                stack.append(ch)
            else:
                if stack and stack[-1] == mappings[ch]:  # for case s = "["
                    stack.pop()
                else:   # for case s = ")(){}"
                    return False

        return len(stack) == 0


solution = Solution()
s = "()[]{}"
assert solution.isValid(s) == True
s = ")(){}"
assert solution.isValid(s) == False
