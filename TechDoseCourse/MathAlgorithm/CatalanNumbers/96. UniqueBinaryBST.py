class Solution:
    def numTrees(self, n: int) -> int:
        """
        This is a catalan numbers problem. There can be 1 BST n=1 i.e. there is a single node.
        There can be 2 bsts if n=2, similarly for n=3, number of BSTs are 5.
        """
        catalanNumbers = [0] * (n + 1)
        catalanNumbers[0] = 1
        catalanNumbers[1] = 1

        for i in range(2, n + 1):
            catalanNumbers[i] = 0

            for j in range(0, i):
                catalanNumbers[i] += catalanNumbers[j] * catalanNumbers[i - j - 1]

        return catalanNumbers[n]


solution = Solution()
print(solution.numTrees(4))