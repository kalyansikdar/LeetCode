# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # This map is to track all created clone nodes
        oldToNewMap = {}

        # using recursion stack
        return self.dfs(node, oldToNewMap)

    def dfs(self, node, oldToNewMap):
        """
        This function returns clone of the graph
        Time Complexity: O(N), N = E + V, accessing the nodes and vertices once
        """
        if node in oldToNewMap:
            return oldToNewMap[node]
        else:
            # if clone already not available, make a new clone and return it
            cloneNode = Node(node.val)
            oldToNewMap[node] = cloneNode

        # once a clone node is created, populate it's neighbors
        for nei in node.neighbors:
            cloneNode.neighbors.append(self.dfs(nei, oldToNewMap))

        return cloneNode



