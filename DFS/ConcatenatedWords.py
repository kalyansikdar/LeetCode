from typing import List


class Solution:
    def findAllConcatenatedWordsInADict_brute_force(self, words: List[str]) -> List[str]:
        mappings = set()

        for word in words:
            mappings.add(word)

        result = []

        for word in words:
            if self.isConcatenatedWord(word, mappings):
                result.append(word)

        return result

    def isConcatenatedWord(self, word, mappings):
        if len(word) == 0:
            return False

        for i in range(1, len(word)):
            left = word[:i]
            right = word[i:]

            if left in mappings and right in mappings:
                return True

            if left in mappings and self.isConcatenatedWord(right, mappings):
                return True

        return False


solution = Solution()
input = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
assert solution.findAllConcatenatedWordsInADict_brute_force(input) == ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
assert solution.findAllConcatenatedWordsInADict_brute_force([""]) == []