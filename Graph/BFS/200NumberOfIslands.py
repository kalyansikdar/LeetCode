class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        visited = set()
        islandCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islandCount += 1

        return islandCount

    def bfs(self, grid, i, j, visited):
        queue = [(i, j)]
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        while queue:
            row, col = queue.pop(0)
            visited.add((row, col))

            for d in directions:
                r, c = row + d[0], col + d[1]

                if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or (r, c) in visited or grid[r][c] == '0':
                    continue
                else:
                    queue.append((r, c))
                    visited.add((r, c))


solution = Solution()
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
assert solution.bfs(grid) == 1
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
assert solution.bfs(grid) == 3
