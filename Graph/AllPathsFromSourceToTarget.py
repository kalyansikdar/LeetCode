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


solution = Solution()
graph =  [[1,2], [3], [3], []]
print(solution.allPathsSourceTarget(graph))
print(solution.allPathsSourceTarget_iterative(graph))