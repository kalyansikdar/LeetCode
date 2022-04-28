class Solution:
    def allPathsSourceTarget_iterative(self, graph):
        N = len(graph) - 1
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop()
            for n in graph[path[-1]]:
                if n == N:
                    ans.append(path + [n])
                else:
                    paths.append(path + [n])
        return ans

    def allPathsSourceTarget_iterative2(self, graph):
        # This is looking for all paths, hence, need to apply DFS
        # For shortest path finding problems, we should use BFS
        # add the starting node, path tuple to the stack

        stack = [(0, [0])]
        destinationIndex = len(graph) - 1
        allPaths = []

        while stack:
            node, currPath = stack.pop()

            if node == destinationIndex:
                temp = currPath.copy()
                allPaths.append(temp)

            for neighbor in graph[node]:
                stack.append((neighbor, currPath + [neighbor]))
                # add the neighbors as elements in stack with their path

        return allPaths

    def allPathsSourceTarget_recursive(self, graph):
        allPaths = []
        if not graph:
            return allPaths
        else:
            self.dfs(graph, 0, [0], len(graph) - 1, allPaths)

        return allPaths

    def dfs(self, graph, idx, currPath, destinationIdx, allPaths):
        if idx == destinationIdx:
            allPaths.append(currPath)

        for v in graph[idx]:
            self.dfs(graph, v, currPath + [v], destinationIdx, allPaths)


solution = Solution()
graph = [[1, 2], [3], [3], []]
assert solution.allPathsSourceTarget_iterative(graph) == [[0, 2, 3], [0, 1, 3]]
assert solution.allPathsSourceTarget_iterative2(graph) == [[0, 2, 3], [0, 1, 3]]
assert solution.allPathsSourceTarget_recursive(graph) == [[0, 1, 3], [0, 2, 3]]
