from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Do a binary search on each row, if the target is found return True, if not, next row
        If at the end of last row, target is not found return False
        TC: NlogN (logN for binary search)
        """
        for i in matrix:
            idx = self.binarySearch(i, 0, len(i) - 1, target)
            if idx != -1:
                return True

        return False

    def binarySearch(self, arr, start, end, target):
        mid = (start + end) // 2

        while start <= end:
            if arr[mid] == target:
                return mid

            if target < arr[mid]:
                return self.binarySearch(arr, start, mid - 1, target)

            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, end, target)

        return -1


solution = Solution()
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
assert solution.searchMatrix(matrix, 19) == True
assert solution.searchMatrix(matrix, 20) == False
