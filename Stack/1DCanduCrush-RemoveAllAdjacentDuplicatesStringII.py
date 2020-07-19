class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            count = k
            if not stack or stack[-1][0] != ch:
                stack.append((ch, 1))
            else:
                top = stack[-1]
                topCount = top[1]
                stack.append((ch, topCount + 1))

                if topCount + 1 == count:
                    while count:
                        stack.pop()
                        count -= 1

        result = [i[0] for i in stack]

        return "".join(result)


solution = Solution()
s = "deeedbbcccbdaa"
k = 3
print ('Result: ', solution.removeDuplicates(s, k))