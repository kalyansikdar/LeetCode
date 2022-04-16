# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        else:
            self.getLevelOrderTraversal(root, 0, result)
            return result

    def getLevelOrderTraversal(self, root, level, result):
        if root:
            if len(result) == level:
                result.append([])

            result[level].append(root.val)

            self.getLevelOrderTraversal(root.left, level + 1, result)
            self.getLevelOrderTraversal(root.right, level + 1, result)

    def levelOrder(self, root):
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)

        while queue:
            size = len(queue)
            # get new level list for each level
            level = []
            # at each level process every node, print it and add its children into the queue
            # for loop ranging queue size tackles all nodes in the level
            for i in range(size):
                popped = queue.pop(0)

                level.append(popped.val)

                # ignore null nodes
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)

            result.append(level)

        return result