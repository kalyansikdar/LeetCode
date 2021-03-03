class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps = ""
        lpsLen = 0
        palindromes = []

        for i in range(0, len(s)):
            for j in range(0, len(s)):
                if self.isPalindrome(s, i, j):
                    palindromes.append(s[i : j + 1])
                    if (j - i + 1) > lpsLen:
                        lpsLen = j - i + 1
                        lps = s[i : j + 1]

        sortedP = sorted(palindromes, key=lambda x: len(x))
        print(sortedP)
        return sortedP[-1]

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
s = "babad"
assert solution.longestPalindrome(s) == "bab"
