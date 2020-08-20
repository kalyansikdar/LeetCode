class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        result = [[1]]

        for i in range(1, numRows):
            row = [1]   # every row always starts with 1
            for j in range(1, i):
                row.append(result[i - 1][j - 1] + result[i - 1][j])
            row.append(1)   # rows end with 1 as well
            result.append(row)
        return result


solution = Solution()
num = 5
print (solution.generate(num))