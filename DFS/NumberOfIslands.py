from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noOfIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.markIsland(grid, i, j)
                    noOfIslands += 1

        return noOfIslands

    def markIsland(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '2'

        self.markIsland(grid, i + 1, j)
        self.markIsland(grid, i - 1, j)
        self.markIsland(grid, i, j + 1)
        self.markIsland(grid, i, j - 1)


solution = Solution()
grid1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
grid2 = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
assert solution.numIslands(grid1) == 1
assert solution.numIslands(grid2) == 3