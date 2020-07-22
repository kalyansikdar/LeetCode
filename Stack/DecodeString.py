class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ''
        currNum = 0

        for ch in s:
            if ch == '[':
                stack.append(currStr)
                stack.append(currNum)
                currStr = ''
                currNum = 0
            elif ch == ']':
                tempNum = stack.pop()
                prevStr = stack.pop()

                currStr = prevStr + tempNum * currStr

            elif ch.isdigit():
                currNum = currNum * 10 + int(ch)
            else:
                currStr += ch

        return currStr


solution = Solution()
s = "3[a]2[bc]"     # output: "aaabcbc"
s = "2[abc]3[cd]ef"     # output:  "abcabccdcdcdef"
print (solution.decodeString(s))