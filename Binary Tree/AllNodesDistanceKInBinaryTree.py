# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.adjList = {}

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        Algorithm: Create a graph by creating an adjacency list
        Then do a BFS. In BFS, for every depth, it checks all the nodes.
        """
        result = []
        if not root:
            return []
        elif K == 0:
            return [target.val]
        else:
            self.convertToGraph(root)
            depth = 0
            queue = [target]
            visited = set()

            while queue and depth <= K:
                # as for every depth we are accessing all the nodes, going over all nodes at any depth
                for _ in range(len(queue)):
                    curr = queue.pop(0)

                    if curr not in visited:
                        visited.add(curr)
                        for node in self.adjList[curr]:
                            # optimization: lets not add any node, if it's already there. Though visited is taking
                            # care of this, but still this check will save some time
                            if node not in queue:
                                queue.append(node)

                        if depth == K:
                            result.append(curr.val)

                depth += 1

            return result

    def convertToGraph(self, root):
        queue = [root]

        while queue:
            curr = queue.pop(0)

            if curr not in self.adjList:
                self.adjList[curr] = []

            if curr.left:
                self.adjList[curr].append(curr.left)
                queue.append(curr.left)

                if curr.left not in self.adjList:
                    self.adjList[curr.left] = []
                self.adjList[curr.left].append(curr)

            if curr.right:
                self.adjList[curr].append(curr.right)
                queue.append(curr.right)

                if curr.right not in self.adjList:
                    self.adjList[curr.right] = []
                self.adjList[curr.right].append(curr)