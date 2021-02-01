from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        return self.helper(s, wordSet, {})

    def helper(self, s, wordSet, cache):
        if len(s) == 0:
            return True

        if s in cache:
            return cache[s]

        for i in range(1, len(s) + 1):
            firstPart = s[:i]
            secondPart = s[i:]

            if firstPart in wordSet:
                if self.helper(secondPart, wordSet, cache):
                    cache[secondPart] = True
                    return True

        cache[s] = False
        return False


solution = Solution()
assert solution.wordBreak("leetcode", ["leet","code"]) == True
assert solution.wordBreak("applepenapple", ["apple", "pen"]) == True
assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False