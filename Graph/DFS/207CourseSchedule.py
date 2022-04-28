class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        dependencies = [0] * numCourses

        # find number of prerequisites for each course's
        # TC for this loop O(P), p is no if pre-reqs
        for i in prerequisites:
            dependencies[i[0]] += 1

        stack, visited = [], set()

        # the courses which do not have any prerequisites, are added to the stack to process
        # TC for this loop O(N), N is number of dependencies
        for idx, d in enumerate(dependencies):
            if d == 0:
                stack.append(idx)

        # using dfs algo
        while stack:
            course = stack.pop()
            # when a course is processed, it's added to visited set
            visited.add(course)

            # as a course is processed/completed, check all it's pre-reqs
            # reduce it's dependency from other courses
            # when there is no dependency, add a previously dependent course to stack
            # Time complexity: for each courses in stack, it's iterating over it's prerequisites,
            # hence time complexity: O(NP)
            for p in prerequisites:
                if p[1] == course and dependencies[p[0]] > 0:
                    # as a pre-req course is completed, reducing the dependency count
                    dependencies[p[0]] -= 1
                    # when there is no dependency, a course is added to the stack to process
                    if dependencies[p[0]] == 0:
                        stack.append(p[0])
        # if all courses could be completed, then visited array will have all the courses
        return len(visited) == numCourses


solution = Solution()
numCourses = 6
preRequisites = [[1, 0], [4, 1], [1, 3], [0, 3], [4, 3], [3, 5], [2, 5], [4, 5]]
assert solution.canFinish(numCourses, preRequisites) is True
numCourses2 = 2
preRequisites2 = [[1, 0], [1, 2], [0, 1]]
assert solution.canFinish(numCourses2, preRequisites2) is False
