class Solution:
    def findRedundantConnection(self, edges):
        parentArr = [i for i in range(len(edges) + 1)]
        rankArr = [1 for i in range(len(edges) + 1)]

        for node1, node2 in edges:
            # union(n1, n2) will be 0 if n1 and n2 could not be connected or already connected
            if not self.union(node1, node2, parentArr, rankArr):
                return [node1, node2]

        return []

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
            parentArr[curr] = parentArr[parentArr[curr]]
            curr = parentArr[curr]

        return curr


solution = Solution()
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
assert solution.findRedundantConnection(edges) == [1, 4]
