class Solution:
    def exist(self, board, word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])

        for i in range(rowLen):
            for j in range(colLen):
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0):
                    return True

        return False

    def dfs(self, board, word, i, j, wordIdx):
        if wordIdx == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIdx] != board[i][j]:
            return False

        # while checking for neighbors, same letter cannot be used again, hence making it "" and then putting it back
        # for further iterations
        temp = board[i][j]
        board[i][j] = ""

        if (self.dfs(board, word, i, j + 1, wordIdx + 1)
                or self.dfs(board, word, i - 1, j, wordIdx + 1)
                or self.dfs(board, word, i + 1, j, wordIdx + 1)
                or self.dfs(board, word, i, j - 1, wordIdx + 1)):
            return True

        board[i][j] = temp
        return False


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCCED"
word = "SCS"

solution = Solution()
print(solution.exist(board, word))
####### Hatke test case ########
# [["C","A","A"],["A","A","A"],["B","C","D"]]
# "AAB"
# expected answer: True
