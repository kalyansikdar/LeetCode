import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []   # min heap

        for i in range(len(mat)):
            heapq.heappush(heap, (sum(mat[i]), i))

        result = []
        # popping from min-heap as it will return in increasing order
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


solution = Solution()
matrix = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

assert solution.kWeakestRows(matrix, k=3) == [2,0,3]