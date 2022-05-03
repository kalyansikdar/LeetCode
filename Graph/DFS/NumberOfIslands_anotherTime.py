from typing import List


class Solution:
    """
    Another one is better solution
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, i, j):
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for dir in directions:
            x, y = i + dir[0], j + dir[1]

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                continue

            if grid[x][y] == '1':
                grid[x][y] = '0'
                self.dfs(grid, x, y)


solution = Solution()
grid1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
grid2 = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
assert solution.numIslands(grid1) == 1
assert solution.numIslands(grid2) == 3