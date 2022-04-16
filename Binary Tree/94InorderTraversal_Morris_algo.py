# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # Morris traversal
        # Algorithm:
        # if root does not have left, it's the left most node, visit it and go right
        # if root has left, mark left subtree as predecessor
        # go to left subtree, then find the right most node in the subtree
        # if it's not pointing to NULL, i.e. we visited this for the first time, link it with current
        # if it's not pointing to NULL/pointing to root, we are visiting it for second time
        # Visit the node, de-link it from root, go left from current
        """
        Time complexity: O(N) as it's traversing all nodes. But runtime is more for this method as it's finding the
        predecessor two times for each node
        Space complexity: O(1) as no stack/recursion stack is being used to maintain the which node to go back after
        a node is completely visited (ignore the result array)
        """
        curr = root
        result = []

        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right

            else:
                # assign left subtree to predecessor
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right
                # Visiting for first time, link it with curr
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                # visiting for second time, visit it, de-link it with curr, move to left subtree
                else:
                    result.append(curr.val)
                    # de-link the predecessor from current
                    pred.right = None
                    curr = curr.right

        return result


"""    
Note: To even improve the solution, the time complexity can be reduced as well. But it requires the tree to not change
frequently. If the nodes are linked with it's predecessors during pre-processing. Later while searching the nodes,
it's fasten to find. These are called 'Threaded binary tree'.
"""