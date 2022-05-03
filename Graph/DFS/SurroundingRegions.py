from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Algo:
        1. Update all zeros in first and last row and column to 'A' and run dfs from each region. It will mark all the
        regions connected to the border regions.
        2. Once all the A's are marked, rest '0' are the regions which are surrounded.
        3. We can mark all O as X
        4. Mark all 'A' to 'O', just to take the regions to initial state
        """
        if len(board) <= 2:
            return

        if len(board[0]) <= 2:
            return

        # only first and last row and column
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1):
                    self.dfs(board, i, j)

        print(board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

        return board

    def dfs(self, board, i, j):
        if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = 'A'

            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i, j - 1)


solution = Solution()
board = [["X","X","X","O","X"], ["X","X","0","X","0"], ["X","X","0","0","0"], ["0","X","X","X","X"], ["X","X","0","0","X"], ["X","X","X","X","X"]]
expectedResult = [["X","X","X","O","X"],["X","X","0","X","0"],["X","X","0","0","0"],["0","X","X","X","X"],["X","X","0","0","X"],["X","X","X","X","X"]]
board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
expectedResult2 = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
assert solution.solve(board) == expectedResult
assert solution.solve(board1) == expectedResult2