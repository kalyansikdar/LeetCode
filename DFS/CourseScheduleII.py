class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        preReqTracker = [0 for i in range(numCourses)]
        stack, visited = [], []

        for i in prerequisites:
            preReqTracker[i[0]] += 1      # tracks how many prerequisites for each courses

        for idx, i in enumerate(preReqTracker):
            if i == 0:      # if any course does not have any prerequisite it can be added to the queue
                stack.append(idx)

        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.append(curr)

            for i in prerequisites:
                if curr == i[1]:
                    preReqTracker[i[0]] -= 1      # because the prerequisite is fulfill now
                    if preReqTracker[i[0]] == 0 and i[0] not in stack:
                        stack.append(i[0])

        if len(visited) == numCourses:
            return visited
        else:
            return []


solution = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print('Result: ', solution.findOrder(numCourses, prerequisites))