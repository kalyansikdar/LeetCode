class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        count_arr = [0 for i in range(numCourses)]
        stack, visited = [], []

        # Concept is we have keep track of number of prerequisites required for each courses. If no pre-requisite
        # required, then that course can be added to the stack.
        for i in prerequisites:
            count_arr[i[0]] += 1

        for i in range(len(count_arr)):
            if count_arr[i] == 0:
                stack.append(i)

        while stack:
            element = stack.pop()

            if element not in visited:
                visited.append(element)
            # for every element popped(course considered complete), find all the courses where that element was
            # pre-req, and decrease 1 from the count_arr because one pre-req is less
            for i in prerequisites:
                if i[1] == element and count_arr[i[0]] > 0:
                    count_arr[i[0]] -= 1
                    if count_arr[i[0]] == 0:    # whenever count is 0, means the course does not have any pre-req left
                        # and ready to be taken
                        stack.append(i[0])
        # if all courses could be completed, then visited array will have all the courses
        return len(visited) == numCourses


solution = Solution()
numCourses = 6
preRequisites = [[1,0],[4,1],[1,3],[0,3],[4,3],[3,5],[2,5],[4,5]]
numCourses2 = 2
preRequisites2 = [[1,0],[1,2],[0,1]]
result = solution.canFinish(numCourses2, preRequisites2)
print (result)
