class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # to check possible odd-length palindromes, starting with a char
            count += self.countPalindromeAroundCenter(s, i, i)
            # to check possible even-length palindromes, starting with a pair
            count += self.countPalindromeAroundCenter(s, i, i + 1)

        return count

    def countPalindromeAroundCenter(self, s, start, end):
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

            count += 1

        return count


solution = Solution()
assert solution.countSubstrings("racecar") == 10
# [r, a, c, e, cec, aceca, racecar, c, a, r]
assert solution.countSubstrings("aaa") == 6
# [a, aa, a, aa, aaa, a]
assert solution.countSubstrings("abc") == 3