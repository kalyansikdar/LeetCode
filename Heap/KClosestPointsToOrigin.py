import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distanceList = []
        heapq.heapify(distanceList)     # creates a min-heap
        for point in points:
            # pushing values in negative basically turns the heap into a max heap
            heapq.heappush(distanceList, (-self.findDistanceFromOrigin(point), point))
            # pop from the max heap whenever the size is greater than K, hence, maintaining smallest K size distances
            if len(distanceList) > K:
                heapq.heappop(distanceList)

        result = [i[1] for i in distanceList]

        return result

    def findDistanceFromOrigin(self, point):
        """
        Distance formula = √(x−0)^2+(y−0)^2 = √(x)^2+(y)^2 = √(x^2+y^2)
        """
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)

        return distance