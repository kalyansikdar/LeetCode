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
                if stack and stack[-1] == mappings[ch]:     # for case s = "["
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


solution = Solution()
s = "()[]{}"
print ('Result: ', solution.isValid(s))