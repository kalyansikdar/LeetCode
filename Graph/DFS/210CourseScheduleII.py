class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # Algorithm explained in Course schedule 1 problem
        dependencies = [0] * numCourses

        # O(p), p is prerequisites
        for course, prereq in prerequisites:
            dependencies[course] += 1

        stack, visited = [], []

        # O(N), N is number of courses
        for idx, d in enumerate(dependencies):
            if d == 0:
                stack.append(idx)

        # for each courses in stack, it's iterating over it's prerequisites, hence time complexity: O(NP)
        while stack:
            course = stack.pop()

            if course in visited:
                return []
            else:
                visited.append(course)

            for c, prereq in prerequisites:
                if prereq == course and dependencies[c] > 0:
                    dependencies[c] -= 1

                    if dependencies[c] == 0:
                        stack.append(c)

        if len(visited) == numCourses:
            return visited
        else:
            return []


solution = Solution()
numCourses = 6
preRequisites = [[1, 0], [4, 1], [1, 3], [0, 3], [4, 3], [3, 5], [2, 5], [4, 5]]
assert solution.findOrder(numCourses, preRequisites) == [5, 2, 3, 0, 1, 4]
numCourses = 5
preRequisites = [[1, 0], [2, 1], [1, 3], [4, 2]]
assert solution.findOrder(numCourses, preRequisites) == [3, 0, 1, 2, 4]
numCourses = 3
preRequisites = [[1, 0], [1, 2], [0, 1]]
assert solution.findOrder(numCourses, preRequisites) == []
