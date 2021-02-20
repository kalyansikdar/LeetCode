import heapq
from typing import List


class Solution:
    def twoCitySchedCost(self, costs) -> int:
        if not costs:
            return None
        costDiff = {}
        minimumCost = 0

        for i in range(len(costs)):
            costDiff[i] = costs[i][1] - costs[i][0]

        sorted_costDiff = sorted(costDiff.items(), key=lambda kv: kv[1], reverse=True)

        serial = [i[0] for i in sorted_costDiff]

        i = 0
        while i < len(serial) // 2:
            minimumCost += costs[serial[i]][0]
            i += 1

        while i < len(serial):
            minimumCost += costs[serial[i]][1]
            i += 1

        return minimumCost

    def twoCitySchedCost_better_but_more_time(self, costs: List[List[int]]) -> int:
        """
         Time complexity:
         Going over the costs list - O(N), at each iteration insert into heap - O(1) to O(logN)
         complexity ~ overall O(nlogn)
         Then going over the heap and poping elements - O(Nlogn). While heapify is called making it O(nlogn)
         Overall - O(nlogn)

         Space complexity: extra heap - O(N)
        """
        # error checking
        if not costs:
            return 0

        # create heap with cost difference
        heap = []
        minCost = 0
        totalLen = len(costs)

        for i in range(len(costs)):
            heapq.heappush(heap, [(costs[i][1] - costs[i][0]), costs[i]])

        # get values from heap and add to cost
        while len(heap) > 0:
            if len(heap) > (totalLen // 2): # taking first n/2 and last n/2 works because
                minCost += heapq.heappop(heap)[1][1]
            else:
                minCost += heapq.heappop(heap)[1][0]

        return minCost

    def twoCitySchedCost_fastest(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[1] - x[0])    # sort is O(nlogn) on both overage and worst case
        minCost = 0
        n = len(costs)

        for c in costs[:n // 2]:    # O(n/2)
            minCost += c[1]

        for c in costs[n // 2:]:    # O(n/2)
            minCost += c[0]
        # Overall TC: O(NlogN)
        return minCost


solution = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
assert solution.twoCitySchedCost(costs) == 110
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
assert solution.twoCitySchedCost(costs) == 1859
costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
assert solution.twoCitySchedCost(costs) == 3086
