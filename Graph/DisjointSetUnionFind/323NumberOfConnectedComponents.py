from typing import List


class Solution:
    def __init__(self, n):
        self.parentArr = [i for i in range(n)]
        self.rankArr = [1]*n

    def countComponents(self, n: int, edges: List[List[int]]):
        # initially before union, all nodes were disconnected, hence, number of disconnected graphs are equal to number
        # of nodes

        result = n
        for node1, node2 in edges:
            if self.union(node1, node2) == 1:
                result -= 1
            # else: if union is not done, number of disconnected graphs do not decrease

        return result

    def union(self, nodeX, nodeY):
        """
        Algorithm for union:
        1. find the parent for both nodes
        2. If rank of a parent is higher, it has more nodes connected to it. Hence, connect the smaller node to it
        3. Once it's connected, parent with higher rank would be the new parent of the other node
        4. Parent with higher rank will have even higher rank as other node's rank is added to it
        5. Return 1 if union is done, otherwise return 0
        """
        parentX = self.find(nodeX)
        parentY = self.find(nodeY)

        # if parent is same, the nodes belong to the same graph, no union required
        if parentX == parentY:
            return 0

        if self.rankArr[parentY] > self.rankArr[parentX]:
            self.parentArr[parentX] = parentY
            self.rankArr[parentY] += self.rankArr[parentX]

        else:
            self.parentArr[parentY] = parentX
            self.rankArr[parentX] += self.rankArr[parentY]

        # 1 indicates that the union between the nodes is completed
        return 1

    def find(self, node):
        """
        Loop through the parent arr to find the ultimate parent of a node
        """
        curr = node
        while curr != self.parentArr[curr]:
            # path compression
            self.parentArr[curr] = self.parentArr[self.parentArr[curr]]
            curr = self.parentArr[curr]

        return curr

    def find_recursive(self, node):
        # base case
        if self.parentArr[node] == node:
            return node

        parent = self.parentArr[node]
        return self.find(parent)


n = 5
solution = Solution(n)
edges = [[0, 1], [1, 2], [3, 4], [0, 2]]
assert solution.countComponents(5, edges) == 2
