from typing import List


class Obj:
    def __init__(self, word, seqNo):
        self.word = word
        self.seqNo = seqNo


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        queue = []
        queue.append(Obj(beginWord, 1))
        wordList = set(wordList)

        while queue:
            curr = queue.pop(0)
            currWord, currSeqNo = curr.word, curr.seqNo
            if currWord == endWord:
                return currSeqNo

            for i in range(len(currWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    adjacentWord = currWord[:i] + c + currWord[i + 1 :]
                    if adjacentWord in wordList:
                        wordList.remove(adjacentWord)
                        queue.append(Obj(adjacentWord, currSeqNo + 1))

        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        This implementation is using tuple instead of an object. Here, at first it's being checked if endWord is in
        wordSet, hence we can return from with in the for loop.
        """
        queue = []
        queue.append((beginWord, 1))
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        while queue:
            curr = queue.pop(0)
            currWord, currSeqNo = curr[0], curr[1]

            for i in range(len(currWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    adjacentWord = currWord[:i] + c + currWord[i + 1 :]
                    # skipping if the adjacent word is same as current word, words are not repeated
                    if adjacentWord == currWord:
                        continue

                    if adjacentWord == endWord:
                        return currSeqNo + 1

                    if adjacentWord in wordSet:
                        wordSet.remove(adjacentWord)
                        queue.append((adjacentWord, currSeqNo + 1))

        return 0


solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
assert solution.ladderLength(beginWord, endWord, wordList) == 5
wordList = ["hot", "dot", "dog", "lot", "log"]
assert solution.ladderLength(beginWord, endWord, wordList) == 0
beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]
assert solution.ladderLength(beginWord, endWord, wordList) == 2
