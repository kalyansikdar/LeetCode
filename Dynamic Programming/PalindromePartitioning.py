from typing import List


class Solution:
    def __init__(self):
        self.tempRes = []

    def partition(self, s: str) -> List[List[str]]:
        result = []

        self.dfs(s, [], result)
        return result

    def dfs(self, s, path, result):
        if len(s) == 0:
            result.append(path)
        # complexity: for len(s) = n, there will be n-1 partitions, you can partition 2^(n - 1) ways
        # For checking palindrome it's O(n), overall O(n2^n)
        for i in range(1, len(s) + 1):
            left = s[:i]
            right = s[i:]

            if self.isPalindrome(left):
                self.dfs(right, path + [left], result)

    def isPalindrome(self, s):
        # this function is O(n)
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
        return True


solution = Solution()
assert solution.partition("aab") == [["a","a","b"],["aa","b"]]
assert solution.partition("aabba") == [["a","a","b","b","a"],["a","a","bb","a"],["a","abba"],["aa","b","b","a"],["aa","bb","a"]]