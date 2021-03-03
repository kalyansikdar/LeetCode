class Solution:
    def isValidSudoku(self, board) -> bool:
        return (
            self.isRowValid(board)
            and self.isRowValid(zip(*board))
            and self.isBlockValid(board)
        )

    def isRowValid(self, board):
        for row in board:
            holder = []
            for col in row:
                if col != ".":
                    holder.append(col)
            if len(holder) != len(set(holder)):
                return False

        return True

    def isBlockValid(self, board):
        ranges = [0, 3, 6]
        # This part is a bit tricky
        for i in ranges:
            for j in ranges:
                # you are creating 2D list for each ranges
                block = [board[a][b] for a in range(i, i + 3) for b in range(j, j + 3)]
                holder = []
                for row in block:
                    if row != ".":
                        holder.append(row)
                if len(holder) != len(set(holder)):
                    return False
        return True


solution = Solution()
board1 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board2 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
result = solution.isValidSudoku(board2)
print(result)
