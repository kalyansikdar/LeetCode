class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s

        res = ""

        for i in range(len(s)):
            len1 = self.findPalindromeLength(s, i, i)
            len2 = self.findPalindromeLength(s, i, i + 1)

            longer_len = max(len1, len2)
            start = i - (longer_len - 1)//2
            end = i + longer_len//2
            possiblePalindrome = s[start: end+1]
            # longer palindrome should replace the smaller one
            if len(possiblePalindrome) > len(res):
                res = possiblePalindrome

        return res

    def longestPalindrome_slightly_different(self, s: str) -> str:
        # Time complexity is O(N^2) here as it's going over the input once - O(N). Finding palindrome adds O(N) to it
        if not s:
            return ""
        if len(s) == 1:
            return s

        length = 0

        for i in range(len(s)):
            len1 = self.findPalindromeLength(s, i, i)
            len2 = self.findPalindromeLength(s, i, i + 1)

            if max(len1, len2) > length:
                i_val = i
                length = max(len1, len2)

        start = i_val - (length - 1) // 2
        end = i_val + length // 2

        return s[start:end + 1]

    def findPalindromeLength(self, s, start, end):
        """Time complexity of this function is O(N) as it's trying to go through the whole input"""
        # concept is to start from the middle and expand out
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        return end - start - 1  # because the start and end is moved left and right after finding the palindrome

    def longestPalindrome_brute_force(self, s: str) -> str:
        # TC: O(N^3) as it's going over the string twice - O(N^2), and checking palindrome adds O(N) to it.
        lps = ""
        lpsLen = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    if (j - i + 1) > lpsLen:
                        lpsLen = j - i + 1
                        lps = s[i:j + 1]

        return lps

    def isPalindrome(self, s, start, end):
        if not s:
            return True

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True


solution = Solution()
s = "racecar"
s = "babbcxcbbabb"
result = solution.longestPalindrome(s)
print (result)
assert solution.longestPalindrome("babad") == "bab"
assert solution.longestPalindrome_brute_force("babad") == "bab"
