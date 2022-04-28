class Solution:
    def findCircleNum(self, isConnected) -> int:
        parentArr = [i for i in range(len(isConnected))]
        rankArr = [1] * len(isConnected)

        numberOfProvinces = len(isConnected)
        visited = set()

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                # Adding restrictions before calling union function
                # visited array is an optimization on cases where (j, i) is already an edge
                # even if the edge is already created, union function would have returned 0
                # but we are restricting it from calling the union at all
                if i != j and isConnected[i][j] == 1 and (i, j) not in visited:
                    if self.union(i, j, parentArr, rankArr):
                        numberOfProvinces -= 1
                        visited.add((j, i))

        return numberOfProvinces

    def union(self, node1, node2, parentArr, rankArr):
        parent1 = self.find(node1, parentArr)
        parent2 = self.find(node2, parentArr)

        if parent1 == parent2:
            return 0

        if rankArr[parent1] >= rankArr[parent2]:
            parentArr[parent2] = parent1
            rankArr[parent1] += rankArr[parent2]
        else:
            parentArr[parent1] = parent2
            rankArr[parent2] += rankArr[parent1]

        return 1

    def find(self, node, parentArr):
        curr = node

        while curr != parentArr[curr]:
            curr = parentArr[curr]

        return curr


solution = Solution()
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
assert solution.findCircleNum(isConnected) == 2
