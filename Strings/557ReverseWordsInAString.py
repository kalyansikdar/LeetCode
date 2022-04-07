class Solution:
    def reverseWords(self, s: str) -> str:
        resultStr = ""
        # end also starts from 0, finds the space to point to the end of a word
        start, end = 0, 0

        while end < len(s):
            # if end is a space, found a word, reverse it
            if s[end] == ' ':
                x = self.reverseStr(s[start: end])
                resultStr += self.reverseStr(s[start: end])
                # add a space after the reversed word
                resultStr += " "
                # move start to the next word starting index
                start = end + 1

            end += 1

        # while loop end before the last word, reverse the last word and add to the result
        resultStr += self.reverseStr(s[start: end])

        return resultStr

    def reverseStr(self, s):
        s = list(s)
        start, end = 0, len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return "".join(s)


solution = Solution()
s = "Let's take LeetCode contest"
assert solution.reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"