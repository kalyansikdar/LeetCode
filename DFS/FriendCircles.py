from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] == 1:
                    count += 1
                    M[i][j] = 0
                    M[j][i] = 0
                    self.dfs(M, j)

        return count

    def findCircleNum_better(self, M: List[List[int]]) -> int:
        count = 0
        for i in range(len(M)):
            # if any diagonal is 1, checking that ith row, if those are connected to the current node
            if M[i][i] == 1:
                count += 1
                self.dfs(M, i)  # so if M[0][0] is 1, then it starts dfs from M[0] (0th row), then M[1] (first row)

        return count

    def dfs(self, M, i):
        for a in range(len(M[i])):
            if M[i][a] == 1:
                M[i][a] = 0
                self.dfs(M, a)


solution = Solution()
M = [[1,1,0],[1,1,0],[0,0,1]]
assert (solution.findCircleNum(M) == 2)
M = [[1,1,0], [1,1,1], [0,1,1]]
assert (solution.findCircleNum_better(M) == 1)