class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s

        res = ""

        for i in range(len(s)):
            len1 = self.checkPalindrome(s, i, i)
            len2 = self.checkPalindrome(s, i, i + 1)

            longer_len = max(len1, len2)
            start = i - (longer_len - 1)//2
            end = i + longer_len//2
            possiblePalindrome = s[start: end+1]
            # longer palindrome should replace the smaller one
            if len(possiblePalindrome) > len(res):
                res = possiblePalindrome

        return res

    def checkPalindrome(self, s, start, end):
        # concept is to start from the middle and expand out
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        return end - start - 1  # because the start and end is moved left and right after finding the palindrome


solution = Solution()
s = "racecar"
s = "babbcxcbbabb"
result = solution.longestPalindrome(s)
print (result)