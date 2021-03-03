from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [
            0 for i in range(len(graph))
        ]  # This list to mark each node with color 1 or -1. No two adjacent
        # node should have the same color

        for i in range(len(graph)):
            # In the given example after first interation itself, all nodes are colored. hence to save time we do not
            # need to check any node if it's already colored
            if colors[i] == 0:
                queue = []
                queue.append(i)
                # once a node is visited, mark it colored 1
                colors[i] = 1

                while queue:
                    node = queue.pop(0)
                    # Need to check all the neighbors of a node, hence for loop
                    for neighbor in graph[node]:
                        # if any node and it's neighbor is of same colo, it means you cannot put those in a separate set
                        if colors[node] == colors[neighbor]:
                            return False

                        elif colors[neighbor] == 0:
                            queue.append(neighbor)
                            # adjacent node of any node is of opposite color: 1 -> -1, -1 -> 1
                            colors[neighbor] = -colors[node]

        return True


solution = Solution()
assert solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) == True
assert solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) == False
