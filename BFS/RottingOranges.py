class Solution:
    def orangesRotting(self, grid) -> int:
        rotten = []
        fresh = []
        minutes = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append([(i, j), minutes])
                elif grid[i][j] == 1:
                    fresh.append([(i, j), minutes])

        if len(fresh) == 0:
            return 0

        while rotten:
            curr = rotten.pop(0)
            minutes = curr[1]
            visited.add(curr[0])

            for dir in directions:
                currI, currJ = curr[0][0] + dir[0], curr[0][1] + dir[1]
                if (
                    currI < 0
                    or currI >= len(grid)
                    or currJ < 0
                    or currJ >= len(grid[0])
                    or grid[currI][currJ] != 1
                    or (currI, currJ) in visited
                ):
                    continue
                else:
                    grid[currI][currJ] = 2
                    rotten.append([(currI, currJ), minutes + 1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes


solution = Solution()
grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]  # output = 4
grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]  # output = -1
grid3 = [[0, 2]]  # output = 0
grid4 = [[0, 2, 2], [0, 2, 1]]  # output 1
print("Result", solution.orangesRotting(grid1))
