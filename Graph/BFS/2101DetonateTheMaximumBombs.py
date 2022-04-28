class Solution:
    def maximumDetonation(self, bombs) -> int:
        # Algorithm:
        # Calculate adjacency map of the bombs
        # Using BFS, find out how many bombs can be denonated for each bomb

        adjMap = self.getNeighbors(bombs)
        result = 0

        for i in range(len(bombs)):
            count = self.findCountByBFS(i, adjMap)
            # if count already max possible value of len(bombs), return it without further calculation
            if count == len(bombs):
                return count

            result = max(result, count)

        return result

    def findCountByBFS(self, index, adjMap):
        visited = set()
        queue = [index]

        while queue:
            bombIdx = queue.pop(0)
            neighbors = adjMap[bombIdx]
            visited.add(bombIdx)

            for i in neighbors:
                if i not in visited:
                    queue.append(i)

        return len(visited)

    def getNeighbors(self, bombs):
        # create adjacency list based on the distance from other bombs
        adjMap = {}

        for i in range(len(bombs)):
            x1 = bombs[i][0]
            y1 = bombs[i][1]
            r1 = bombs[i][2]

            neighbors = []

            for j in range(len(bombs)):
                if i == j:
                    continue

                x2 = bombs[j][0]
                y2 = bombs[j][1]

                distance = self.getDistance(x1, y1, x2, y2)

                # Not using sqrt as it complicates the calculation, instead squaring r1
                if distance <= r1 ** 2:
                    neighbors.append(j)

            adjMap[i] = neighbors

        return adjMap

    def getDistance(self, x1, y1, x2, y2):
        distance = (y2 - y1) ** 2 + (x2 - x1) ** 2
        return distance


solution = Solution()
bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
assert solution.maximumDetonation(bombs) == 5
bombs = [[1, 1, 5], [10, 10, 5]]
assert solution.maximumDetonation(bombs) == 1
bombs = [[2, 1, 3], [6, 1, 4]]
assert solution.maximumDetonation(bombs) == 2
