class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        tracker = [0 for i in range(numCourses)]
        stack, visited = [], []

        for i in prerequisites:
            tracker[i[0]] += 1

        for idx, i in enumerate(tracker):
            if i == 0:
                stack.append(idx)

        while stack:
            element = stack.pop()
            if element not in visited:
                visited.append(element)

            for i in prerequisites:
                if element == i[1]:
                    tracker[i[0]] -= 1
                    if tracker[i[0]] == 0 and i[0] not in stack:
                        stack.append(i[0])

        if len(visited) == numCourses:
            return visited
        else:
            return []