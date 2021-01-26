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

    def longestPalindrome_slightly_different(self, s: str) -> str:
        """Time complexity is O(N) here as it's going over the input once"""
        if not s:
            return ""
        if len(s) == 1:
            return s

        length = 0

        for i in range(len(s)):
            len1 = self.checkPalindrome(s, i, i)
            len2 = self.checkPalindrome(s, i, i + 1)

            if max(len1, len2) > length:
                i_val = i
                length = max(len1, len2)

        start = i_val - (length - 1) // 2
        end = i_val + length // 2

        return s[start:end + 1]

    def checkPalindrome(self, s, start, end):
        """Time complexity of this function is O(N) as it's trying to go through the whole input"""
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
assert solution.longestPalindrome("babad") == "bab"
