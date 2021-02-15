from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0 for i in range(len(graph))]

        for i in range(len(graph)):
            if colors[i] == 0:
                queue = []
                queue.append(i)

                colors[i] = 1

                while queue:
                    node = queue.pop(0)

                    for neighbor in graph[node]:
                        if colors[node] == colors[neighbor]:
                            return False

                        elif colors[neighbor] == 0:
                            queue.append(neighbor)
                            colors[neighbor] = -colors[node]

        return True


solution = Solution()
assert solution.isBipartite([[1,3],[0,2],[1,3],[0,2]]) == True
assert solution.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]) == False