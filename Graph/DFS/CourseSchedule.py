from typing import List


class Solution:
    """
    This problem is basically cycle detection
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adjacency_matrix = [None] * numCourses
        self.visited = [0] * numCourses

        for i in range(numCourses):
            self.adjacency_matrix[i] = []

        # create adjacency matrix
        for pre in prerequisites:
            self.adjacency_matrix[pre[0]].append(pre[1])

        for i in range(numCourses):
            if self.visited[i] == 0 and not self.dfs(i):
                return False

        return True

    def dfs(self, v):
        """
        0 - not processed
        1 - under process
        2 - processed
        """
        # while within the dfs, if there is any node still under process, it means this is a back edge,
        # hence, there is a cycle
        # If there is no back-edge, there is no cycle
        if self.visited[v] == 1:
            return False

        if self.visited[v] == 2:
            return True

        self.visited[v] = 1

        for ad in self.adjacency_matrix[v]:
            if not self.dfs(ad):
                return False

        self.visited[v] = 2

        return True
