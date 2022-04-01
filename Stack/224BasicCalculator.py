class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        currNo = 0
        answer = 0
        stack = []
        i = 0

        # used while loop as within for loop index cannot be updated.
        while i < len(s):
            if s[i].isdigit():
                currNo = int(s[i])
                # this while loop is needed for numbers with multiple digits
                while (i + 1) < len(s) and s[i + 1].isdigit():
                    currNo = currNo * 10 + int(s[i + 1])
                    i += 1

                currNo = currNo * sign
                answer += currNo
                currNo = 0
                sign = 1

            elif s[i] == '+':
                sign = 1

            elif s[i] == '-':
                sign = -1

            elif s[i] == '(':
                stack.append(answer)
                stack.append(sign)
                # reset the answer once it's loaded onto stack
                sign = 1
                answer = 0

            elif s[i] == ')':
                # pop the sign and answer and calculate overall answer
                prevSign = stack.pop()
                answer = prevSign * answer
                prevAnswer = stack.pop()
                answer = prevAnswer + answer

            i += 1

        return answer


solution = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
assert solution.calculate(s) == 23