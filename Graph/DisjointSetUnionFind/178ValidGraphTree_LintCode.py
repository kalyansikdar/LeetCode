from typing import (
    List,
)


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # A graph can be a valid tree for 2 conditions:
        # 1. Graph is not cyclic
        # 2. Graph has only one component
        components = n
        parentArr = [i for i in range(n)]
        rankArr = [1 for i in range(n)]

        for node1, node2 in edges:
            if self.union(node1, node2, parentArr, rankArr) == 0:
                return False
            else:
                components -= 1

        return components == 1

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
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
assert solution.valid_tree(n, edges) == True