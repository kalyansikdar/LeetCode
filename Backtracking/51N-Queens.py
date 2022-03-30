class Solution:
    def __init__(self):
        self.result = []
        self.board = []
        self.columns = set()
        self.positiveDiagnals = set()
        self.negativeDiagnals = set()

    def solveNQueens(self, n: int):

        self.board = [["."] * n for i in range(n)]
        self.backtracking(0, n)
        return self.result

    def backtracking(self, row, n):
        if row == n:
            copyBoard = ["".join(i) for i in self.board]
            self.result.append(copyBoard)
            return

        for col in range(n):
            if col in self.columns or (row + col) in self.positiveDiagnals or (row - col) in self.negativeDiagnals:
                continue

            self.columns.add(col)
            self.positiveDiagnals.add(row + col)
            self.negativeDiagnals.add(row - col)
            self.board[row][col] = "Q"

            self.backtracking(row + 1, n)

            self.columns.remove(col)
            self.positiveDiagnals.remove(row + col)
            self.negativeDiagnals.remove(row - col)
            self.board[row][col] = "."


solution = Solution()
N = 4
expectedResult = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
assert solution.solveNQueens(N) == expectedResult