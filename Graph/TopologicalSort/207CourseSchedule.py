class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solved by topological sort+BFS concept OR Kahn's Algorithm
        # Time complexity O(V+E) as it's visited each node, edge once
        inDegrees = [0 for i in range(numCourses)]
        topologicalSort = []

        for e1, e2 in prerequisites:
            inDegrees[e1] += 1

        queue = []

        for idx, i in enumerate(inDegrees):
            if i == 0:
                queue.append(idx)

        while queue:
            course = queue.pop(0)
            topologicalSort.append(course)

            # removed course from graph, need to reduce indegree for all dependent courses
            for c1, c2 in prerequisites:
                if c2 == course and inDegrees[c1] > 0:
                    # as dependency is removed, decrease the in-degree of dependent node
                    inDegrees[c1] -= 1
                    # if there is no pre-req left, time to visit the course
                    if inDegrees[c1] == 0:
                        queue.append(c1)

        # Check if all the courses are visited
        return len(topologicalSort) == numCourses


solution = Solution()
numCourses = 6
preRequisites = [[1, 0], [4, 1], [1, 3], [0, 3], [4, 3], [3, 5], [2, 5], [4, 5]]
assert solution.canFinish(numCourses, preRequisites) is True
numCourses2 = 2
preRequisites2 = [[1, 0], [1, 2], [0, 1]]
assert solution.canFinish(numCourses2, preRequisites2) is False