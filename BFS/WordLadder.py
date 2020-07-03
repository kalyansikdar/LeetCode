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
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    adjacentWord = currWord[:i] + c + currWord[i + 1:]
                    if adjacentWord in wordList:
                        wordList.remove(adjacentWord)
                        queue.append(Obj(adjacentWord, currSeqNo + 1))

        return 0


solution = Solution()
beginWord = "hit"
endWord = "cog"
wordList =["hot","dot","dog","lot","log","cog"]
print (solution.ladderLength(beginWord, endWord, wordList))