class Solution:
    def __init__(self):
        self.tracker = set()

    def exist(self, board, word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                # initiate by checking for each letters in the board
                if self.dfs(board, i, j, 0, word):
                    return True

        return False

    def dfs(self, board, row, col, wordIndex, word):
        # terminating condition: index reached more than the last char index
        if wordIndex == len(word):
            return True

        # checking bounds. If the word char is not matching the board char -> not a match
        # is the (row, col) combination is already there in tracker -> skip it -> same letter cell not to be
        # used more than once
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[wordIndex] or (
        row, col) in self.tracker:
            return False

        # valid char -> add to tracker
        self.tracker.add((row, col))

        # check for surroundings
        result = self.dfs(board, row + 1, col, wordIndex + 1, word) or self.dfs(board, row - 1, col, wordIndex + 1,
                                                                                word) or self.dfs(board, row, col + 1,
                                                                                                  wordIndex + 1,
                                                                                                  word) or self.dfs(
            board, row, col - 1, wordIndex + 1, word)

        # backtracking
        self.tracker.remove((row, col))

        return result


solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
assert solution.exist(board, word) == True