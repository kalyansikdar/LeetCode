import heapq
class Solution:
    def twoCitySchedCost(self, costs) -> int:
        """
        Time Complexity is O(nlogn) as heapify is called every time an element is popped from heap. heapify is O(nlogn)
        :param costs:
        :return:
        """
        heap = []
        heapq.heapify(heap)
        initialLength, minCost = 0, 0

        for i in range(len(costs)):     # sort the costs based on difference, wherever difference is more that's more
            # cost effective
            heapq.heappush(heap, ((costs[i][0] - costs[i][1]), costs[i]))

        print(heap)
        initialLength = len(heap)       # for first N/2 elements add A costs, second N/2 elements add B costs.
        i = 0
        while heap:     # heap length is declining as we are popping at every step
            if len(heap) > initialLength//2:
                minCost += heapq.heappop(heap)[1][0]    # for first N/2 elements add A costs
                print(i, minCost)
            else:
                minCost += heapq.heappop(heap)[1][1]    # for second N/2 elements add B costs.
                print(i, minCost)

        return minCost


solution = Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
costs = [[20,60],[10, 50],[40, 200],[30, 300]]
print(solution.twoCitySchedCost(costs))